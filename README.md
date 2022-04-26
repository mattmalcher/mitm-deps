# mitm-deps
Attempt to use mitm proxy to gather urls for dependencies pulled from the web by a container.

# Goal
Want an environment, where I can install packages, models etc that transparently routes all requests through a mitm proxy so I can generate a log of exactly what is requested from where.


**Update** - have just used mitm-in-a-box. This required

An update of the makefile to use new mitmproxy syntax

```makefile
$(shell pwd)/certs/mitmproxy-ca-cert.cer:
	@mkdir -p $(shell pwd)/certs
	@mitmdump --set confdir=$(shell pwd)/certs --listen-port 1 2> /dev/null || echo "Certs generated in $(shell pwd)/certs"

```
An update of the Vagrantfile to use a newer box image

```rb
  config.vm.box = "debian/bullseye64"
```

# Refs

https://docs.mitmproxy.org/stable/howto-transparent-vms/

https://softwaretester.info/man-in-the-middle-attack-mitm/

https://gitlab.com/guardianproject/masque-mitm/-/blob/main/proxy-router/Vagrantfile

https://github.com/abeluck/mitm-in-a-box/ - very useful

https://docs.mitmproxy.org/stable/mitmproxytutorial-userinterface/