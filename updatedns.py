#!/usr/bin/env python3

import requests
import os

file_url = "http://rpi.prathamskills.org/Conf/dnsmasq.txt"
path = "/etc/dnsmasq.conf"

r = requests.get(file_url, stream=True)

if os.path.exists(path):
    os.system('sudo rm -r /etc/dnsmasq.conf')
else:
    pass

with open(path, "wb") as dns:
    for chunk in r.iter_content(chunk_size=1024):

        # writing one chunk at a time to file
        if chunk:
            dns.write(chunk)

