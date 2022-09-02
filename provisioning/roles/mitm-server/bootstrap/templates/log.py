from mitmproxy import http
import hashlib
import json
import time

def response(flow):
    url_request: str = str(flow.request.pretty_url)
    url_request = url_request.replace("/", "_")
    hash_string = (
    hashlib.sha1(url_request.encode()).hexdigest()[:10] +
        '_' +
        str(int(time.time())) +
        '.json'
    )

    with open(str('/home/vagrant/req/' + hash_string), "ab") as ofile:
        d = dict()
        d['url'] = str(flow.request.pretty_url.encode())
        d['headers'] = dict(flow.request.headers.items())
        d = json.dumps(d)
        ofile.write(d.encode())

