# Infrastructure-as-a-Code + Narzędzia [Draft]

## Terraform

State-of-the-art. Obecnie Terraform i Terragrunt uznawane za najlepsze narzędzie dla Infrastructure-as-a-Code.

1. Zainstaluj terraform na twoim komputerze według [instrukcji](https://learn.hashicorp.com/tutorials/terraform/install-cli).

2. Korzystając z dokumentacji [Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
) i [przykładów](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/virtual-machines), utwórzmy w następnych krokach maszynę wirtualną.

3. Przygotuj projekt.

   ```bash
   mkdir azure-tf
   cd azure-tf
   touch main.tf
   ```

4. Do `main.tf` przekopiuj definicję providera ([na podstawie przykładu](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/virtual-machines/linux/basic-password)):

   ```terraform
   provider "azurerm" {
     features {}
   }
   ```

   Zanim, pójdziemy dalej zainicjujmy projekt:

   ```bash
   terraform init
   ```

5. Do `main.tf` przekopuj kilka zasobów i uruchom `terraform plan`,

   ```terraform
   provider "azurerm" {
     features {}
   }

   variable "password" {
     description = "The password for the VM to login over ssh"
   }

   resource "azurerm_resource_group" "main" {
     name     = "wsb-resources"
     location = "eastus"
   }

   resource "azurerm_virtual_network" "main" {
     name                = "wsb-network"
     address_space       = ["10.0.0.0/22"]
     location            = azurerm_resource_group.main.location
     resource_group_name = azurerm_resource_group.main.name
   }

   resource "azurerm_subnet" "internal" {
     name                 = "internal"
     resource_group_name  = azurerm_resource_group.main.name
     virtual_network_name = azurerm_virtual_network.main.name
     address_prefixes     = ["10.0.2.0/24"]
   }

   resource "azurerm_public_ip" "public_ip" {
     name                = "wsb-public-ip"
     resource_group_name = azurerm_resource_group.main.name
     location            = azurerm_resource_group.main.location
     allocation_method   = "Dynamic"
   }

   resource "azurerm_network_interface" "main" {
     name                = "wsb-nic"
     resource_group_name = azurerm_resource_group.main.name
     location            = azurerm_resource_group.main.location

     ip_configuration {
       name                          = "internal"
       subnet_id                     = azurerm_subnet.internal.id
       private_ip_address_allocation = "Dynamic"

       public_ip_address_id = azurerm_public_ip.public_ip.id
     }
   }

   resource "azurerm_linux_virtual_machine" "main" {
     name                            = "wsb-vm"
     resource_group_name             = azurerm_resource_group.main.name
     location                        = azurerm_resource_group.main.location
     size                            = "Standard_B1ls"
     admin_username                  = "ubuntu"
     admin_password                  = var.password
     disable_password_authentication = false
     network_interface_ids = [
       azurerm_network_interface.main.id,
     ]

     source_image_reference {
       publisher = "Canonical"
       offer     = "UbuntuServer"
       sku       = "18.04-LTS"
       version   = "latest"
     }

     os_disk {
       storage_account_type = "Standard_LRS"
       caching              = "ReadWrite"
     }
   }
   ```

4. Narzędzia - [tflint](https://github.com/terraform-linters/tflint)

5. Narzędzia - [tfsec](https://github.com/aquasecurity/tfsec)

6. Narzędzia - [infracost](https://github.com/infracost/infracost):

## Docker

Narzędzia - docker:

- dockerfile lint:

  ```bash
  docker run --rm -i hadolint/hadolint Dockerfile

  find . -iname Dockerfile | xargs -I {} bash -c "echo {}; docker run --rm -i hadolint/hadolint < {}"
  ```

- trivy:

  ```bash
  # zeskanujmy stary obraz dockera
  trivy image python:2
  ```
