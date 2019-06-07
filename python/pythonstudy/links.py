import urllib
from BeautifulSoup import *
import json
import ssl

pos = 18#3
times = 7#4
#url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Khayla.html"
for time in range(times):
    print 'Retrieving', url
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    html = urllib.urlopen(url, context=scontext)
    data = html.read()

#html = urllib.urlopen(url).read()
#for line in html:
#    print line
    soup = BeautifulSoup(data)
    tags = soup('a')
    url =  tags[pos-1].get('href',None)
print url
