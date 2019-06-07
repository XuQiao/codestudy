#/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen

import json

jstring=urlopen("https://cmsweb.cern.ch/phedex/datasvc/json/prod/subscriptions?request=535409")
j=json.loads(jstring)
print(j)
