import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location:")
#'http://python-data.dr-chuck.net/comments_42.xml'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//comment')
sum = 0
print 'Counts:', len(results)
for result in results:
    count = int(result.find('count').text)
    sum = sum + count

print sum
