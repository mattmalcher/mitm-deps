# mitm-deps
Setup for download & vetting of model dependency files.

# Goal
Want an environment, where I can install & test packages, models etc and capture relevant info to satisfy myself they arent malicious. It should:

* Route all requests through a proxy so I can generate a log and audit exactly what is requested from where.
* Virus scan files
* Inspect files
	- generate md5s to check against source
	- check for executables

# Overview

## Server
* systemd unit running /usr/local/bin/mitmdump on 8080 
	* `sudo journalctl -u mitmdump`
* dnsmasq acting as DNS server & DHCP Server
	* `sudo journalctl -u dnsmasq`
	* `sudo journalctl -u dnsmasq --follow`
* iptables configured to point traffic from 10.0.3.3 ports 80/443 to the mitm proxy on 127.0.0.1:8080
	* `sudo iptables -S`

## Client
* set up to send its traffic to 10.0.3.3 `ip route replace default via 10.0.3.3 dev eth1`
* uses the stuff in /dep_fetchers to download dependencies
* has clamav installed & updates definitions
* runs get_deps playbook to download and inspect the dependencies.


# To Use

If you run `vagrant up` the entire infrastructure will get stood up.

## Auto

Once everything is up and running you can use: `make run_dep_playbook playbook=provisioning/<relevant playbook>.yml`. The `logs/<dep>/` folder should start filling up with request logs, virus scan results, and file information.

You can re-run make `get_deps` as you develop the dep_fetchers without re-provisioning all the other bits.


## AdHoc

You can also ssh into the server/client machines for tests or ad-hoc tasks. For example:

**Console 1**

```
vagrant ssh mitm-client
curl https://yahoo.com 
```

**Console 2**

```
vagrant ssh mitm-server
mitmproxy -r mitmdump.log --showhost --no-server # view the stored log
```

# Refs

This is heavily based on the [`mitm-in-a-box`](https://github.com/abeluck/mitm-in-a-box) repo with extensions for my use case.

The mitm-in-a-box code has been refactored to:
* reorganised into a single playbook / vagrantfile
* use updated versions of debian, mitm-proxy

## mitmproxy

The following docs were useful:

* https://docs.mitmproxy.org/stable/howto-transparent-vms/
* https://docs.mitmproxy.org/stable/mitmproxytutorial-userinterface/

## Ansible

This ansible role for clamav was valuable:

https://github.com/geerlingguy/ansible-role-clamav 

