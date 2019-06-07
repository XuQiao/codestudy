import json
import urllib

serviceurl = 'http://python-data.dr-chuck.net/comments_207739.json'

uh = urllib.urlopen(serviceurl)
data = uh.read()
info = json.loads(data)
print 'User count:', len(data)
sumc = 0
counts = 0

for item in info['comments']:
    sumc = sumc + item['count']
    counts = counts + 1

print 'Count:', counts
print 'Sum:', sumc
