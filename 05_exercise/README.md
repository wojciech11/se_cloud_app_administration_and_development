# Infrastructure-as-a-Code

## Terraform

0. Zaloguj się na portal Azure-a:

   ```bash
   az login --use-device-code
   ```

1. Zainstaluj terraform na twoim komputerze według [instrukcji](https://learn.hashicorp.com/tutorials/terraform/install-cli).

2. Zainstaluje następujące narzędzia:

   - [infracost](https://www.infracost.io/docs/)
   - [tflint](https://github.com/terraform-linters/tflint)
   - [tfsec](https://github.com/aquasecurity/tfsec)

3. Korzystając z dokumentacji [Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs
) i [przykładów](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/virtual-machines), utwórzmy w następnych krokach maszynę wirtualną.

4. Przygotuj projekt.

   ```bash
   mkdir azure-tf
   cd azure-tf
   touch main.tf
   ```

5. Do `main.tf` przekopiuj definicję providera ([na podstawie przykładu](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples/virtual-machines/linux/basic-password)):

   ```terraform
   provider "azurerm" {
     features {}
   }
   ```

   Zanim, pójdziemy dalej zainicjujmy projekt:

   ```bash
   terraform init
   ```

6. Do `main.tf` przekopuj kilka zasobów i uruchom `terraform plan`,

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
     size                            = "Standard_B9ls"
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

   Niezwykle pomocną komendą jest również `terraform fmt`.


7. A co z jakością naszego Terraforma? `tflint` przychodzi z pomocą. Możemy zainstalować krok po kroku, jak to jest opisane na [githubie projektu](docker pull ghcr.io/terraform-linters/tflint-bundle:latest), albo skorzystać z dockera:

   ```bash
   docker run --rm -v $(pwd):/data -t ghcr.io/terraform-linters/tflint-bundle
   ```

   Popraw błąd, zanim przejdziesz dalej.

8. Zanim zaplikujesz plan, wykorzystaj nowe narzędzia, aby poznać koszt naszej nowej infrastruktury:


   ```bash
   # let's store our plan in a file
   terraform plan -out plan.cache
   infracost breakdown --path plan.cache
    ```

9. A co z najlepszymi praktykami bezpieczeństwa? Skorzystajmy z `tfsec`: 


   ```bash
   tfsec .
   ```

10. Apply:

   ```bash
   terraform apply
   ```

11. Zaloguj się do swojej maszyny:

   ```bash
   ssh ubuntu@X.Y.Z.V
   ```

12. Dodaj tagi ([azure](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json), [aws](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)) do swojej wirtualnej maszyny.

13. Usuń tylko definicję maszyny wirtualnej z `main.tf` i wywołaj `terraform apply`.

14. Dodatkowe:

   - wyświetlij IP address z pomocą [outputs](https://www.terraform.io/docs/language/values/outputs.html)
   - generacja hasła z [password resource](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/password)

15. Usuńmy wszystko:

   ```bash
   terraform destroy
   ```

Zauważ: Moglibyśmy również zainstalować wymagane pakiety z poziomu Terraforma posługując się *Provisioner*, na przykład, [remote-exec](https://www.terraform.io/docs/language/resources/provisioners/remote-exec.html). Więcej informacji znajdziesz w [dokumentacji](https://www.terraform.io/docs/language/resources/provisioners/syntax.html).


## Ansible



