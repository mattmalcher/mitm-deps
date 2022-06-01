
$(shell pwd)/certs/mitmproxy-ca-cert.cer:
	@mkdir -p $(shell pwd)/certs
	@mitmdump --set confdir=$(shell pwd)/certs --listen-port 1 2> /dev/null || echo "Certs generated in $(shell pwd)/certs"

gencerts: $(shell pwd)/certs/mitmproxy-ca-cert.cer

clean:
	@cd certs; rm mitmproxy-ca-cert.cer  mitmproxy-ca-cert.p12  mitmproxy-ca-cert.pem  mitmproxy-ca.pem  mitmproxy-dhparam.pem mitmproxy-ca.p12

default: gencerts

# Run just the get_deps playbook, outside of vagrant but using the vagrant inventory & ignoring host checking.
get_deps:
	ansible-playbook \
	-i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory \
	-u vagrant \
	--ssh-common-args " -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" \
	--private-key '~/.vagrant.d/insecure_private_key' \
	provisioning/get_deps.yml

# use by passing logfile when calling make, for example:
# 	make view_log logfile=logs/spacy.log
view_log:
	mitmproxy -r $(logfile) --showhost --no-server