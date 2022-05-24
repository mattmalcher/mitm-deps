# mitm-deps
Attempt to use mitm proxy to gather urls for dependencies pulled from the web by a container.

This is heavily based on the [`mitm-in-a-box`](https://github.com/abeluck/mitm-in-a-box) repo. The following have changed:
* reorganised into a single playbook and roles
* updated versions

# Goal
Want an environment, where I can install & test packages, models etc that transparently routes all requests through a mitm proxy so I can generate a log and audit exactly what is requested from where.


# To Use

**Console 1**

```
cd mitm-client
vagrant ssh
curl https://yahoo.com # request completes succesfully
```

**Console 2**

```
cd mitm-server
vagrant ssh
mitmproxy -r mitmdump.log --showhost --no-server # view the stored log
```


# Setup

## Server
* systemd unit running /usr/local/bin/mitmdump on 8080 
	* `sudo journalctl -u mitmdump`
* dnsmasq acting as DNS server & DHCP Server
	* `sudo journalctl -u dnsmasq`
	* `sudo journalctl -u dnsmasq --follow`
* iptables configured to point traffic from 10.0.3.3 ports 80/443 to 127.0.0.1:8080
	* `sudo iptables -S`

## Client
* set up to send its traffic to 10.0.3.3? `ip route replace default via 10.0.3.3 dev eth1`



# Debugging

This isnt working yet, and i'm not sure why

## Client DNS
Initially curl from the client times out, but then, after some time it becomes unable to even resolve addresses:

```sh
curl http://google.com

curl: (6) Could not resolve host: google.com
```

dig appears to look at 10.0.3.3 but get **refused**

```sh
vagrant@mitm-client:~$ dig http://google.com

; <<>> DiG 9.16.27-Debian <<>> http://google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 41110
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;http://google.com.             IN      A

;; Query time: 4 msec
;; SERVER: 10.0.3.3#53(10.0.3.3)
;; WHEN: Tue May 24 17:44:03 UTC 2022
;; MSG SIZE  rcvd: 46
```

can ping 10.0.3.3 from client successfully, so I guess becomes a question of why we cant ask it DNS questions?

It looks like dnsmasq is reading the supplied config because its logs inlude:

> mitm-server dnsmasq[10869]: using nameserver 1.1.1.1#53

dig gets answers when run on the server, is there something silly like need to open some ports on the virtualbox?





# Refs

https://docs.mitmproxy.org/stable/howto-transparent-vms/

https://softwaretester.info/man-in-the-middle-attack-mitm/

https://gitlab.com/guardianproject/masque-mitm/-/blob/main/proxy-router/Vagrantfile

https://github.com/abeluck/mitm-in-a-box/ - very useful

https://docs.mitmproxy.org/stable/mitmproxytutorial-userinterface/