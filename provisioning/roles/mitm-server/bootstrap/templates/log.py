from mitmproxy import http
import hashlib
import json
import time

def response(flow):
    url_request: str = str(flow.request.pretty_url)
    url_request = url_request.replace("/", "_")
    time_stamp = str(int(time.time()))
    hash_string = (
    hashlib.sha1(url_request.encode()).hexdigest()[:10] +
        '_' +
        time_stamp +
        '.json'
    )

    with open(str('/home/vagrant/req/' + hash_string), "ab") as ofile:
        d = dict()
        d['url'] = str(flow.request.pretty_url.encode())
        d['time_stamp'] = time_stamp
        d['headers'] = dict(flow.request.headers.items())
        d = json.dumps(d)
        ofile.write(d.encode())

