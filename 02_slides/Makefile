DECKTAPE_VERSION=3

give_me_pdf:
	docker run --rm -v $$(pwd):/slides \
		-v $$(pwd):/home/user astefanutti/decktape:$(DECKTAPE_VERSION) \
		-s 2560x1600 index.html index.pdf

give_me_zip:
	cd .. && zip -r $(CURDIR).zip $(CURDIR)/*
