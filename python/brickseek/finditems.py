import re 
import urllib2
from BeautifulSoup import BeautifulSoup
import csv

def findname(pageid):
    url = "http://brickseek.com/clearance/deals/electronics/?p="+str(pageid)
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    urlo = urllib2.urlopen(req)
    soup = BeautifulSoup(urlo)
    skuAll = soup.findAll('div',text=re.compile(r'SKU:*'))
    sku = []
    for s in skuAll:
        skunumber1 = s.parent.parent.text.replace("SKU:","");
        skunumber = skunumber1.replace(".","");
        if re.search('[a-zA-Z]', skunumber) or re.search('-', skunumber):
            pass
        else:
            sku.append(skunumber)
    return sku

csvfile = open('walmart_skuids.csv', 'wb')
writer = csv.writer(csvfile)
for i in range(1,14):
    s = findname(i)
    for ss in s:
        writer.writerow([ss])   
