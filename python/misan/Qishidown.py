from bs4 import BeautifulSoup
import requests
import sys
import urllib
import os
if sys.version_info[0] == 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlopen

url0 = "https://www.qishicpc.com/media/"

def get_all(url):
    soup = BeautifulSoup(requests.get(url).text,'lxml')
    for a in soup.find_all('a',href=True):
        if not '../' in a:
            print("link=", a)
            yield url + a['href']

def download(urlfile):
    directory = urlfile.replace(url0,"").split('/')[0];
    filename = urlfile.replace(url0,"").split('/')[1];
    print(directory+'/'+filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.isfile(directory+'/'+filename): 
        urllib.request.urlretrieve(urlfile, 'qishimedia'+directory+'/'+filename)

print(url0)
for directory in get_all(url0):
   print(directory)
   directory1 = directory.replace(url0,"").split('/')[0];
   if os.path.exists(directory1):
       continue
   for urlfile in get_all(directory):
      print(urlfile)
      download(urlfile)

