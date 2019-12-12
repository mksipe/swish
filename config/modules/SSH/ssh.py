#!/usr/bin/env python3
import urllib.request

url = 'http://ftp.us.debian.org/debian/pool/main/o/openssh/ssh_7.4p1-10+deb9u7_all.deb'
urllib.request.urlretrieve(url, 'config/core/modules/SSH')