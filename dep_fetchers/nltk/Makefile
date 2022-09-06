get_nltk_data_build:
	cp /usr/local/share/ca-certificates/mitmproxy-ca.crt .
	docker build --network host -t nltk .
get_nltk_data_download:
	docker run -v $(shell pwd):/host --network host --rm nltk

