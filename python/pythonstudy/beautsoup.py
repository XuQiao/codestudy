import urllib
from BeautifulSoup import *

sums = 0
#url = "http://python-data.dr-chuck.net/comments_42.html"
url = "http://python-data.dr-chuck.net/comments_207738.html"
html = urllib.urlopen(url).read()
#for line in html:
#    print line
soup = BeautifulSoup(html)
tags = soup('span')
for tag in tags:
    score = int(tag.contents[0])
    sums = sums + score

print sums
