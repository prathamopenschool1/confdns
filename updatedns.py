#!/usr/bin/env python3

import requests
import os
from zipfile import ZipFile


def upgrade_dns():
    print("wait while list is updating...")

    try:
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

        print("completed")

    except Exception as dns:
        print(dns)


def get_the_zip():
    upgrade_dns()
    try:
        os.system('sudo chmod 777 -R /var/www/')

        zip_file_url = "http://rpi.prathamskills.org/apps/index.zip"
        path_to_put = "/var/www/html/index.zip"

        if os.path.exists(path_to_put):
            os.system('sudo rm -rf /var/www/html/index.zip')
        else:
            pass

        file_to_get = requests.get(zip_file_url)

        with open(path_to_put, "wb") as new_file:
            for chunk in file_to_get.iter_content(chunk_size=1024):
                new_file.write(chunk)

    except Exception as d:
        print(d)

    try:
        file_name = "/var/www/html/index.zip"
        with ZipFile(file_name, 'r') as zip:
            zip.extractall('/var/www/html/')
    except Exception as e:
        print(e)

    print("Done")


get_the_zip()

