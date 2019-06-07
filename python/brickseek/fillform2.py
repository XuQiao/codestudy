#!/usr/bin/python
import re 
import urllib2
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
#from bs4 import BeautifulSoup
import csv

def findname(skuid):
    url = "http://brickseek.com/clearance/deals/all/?q="+skuid
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    urlo = urllib2.urlopen(req)
    soup = BeautifulSoup(urlo)
    name = soup.findAll('h6')[0].text
    name = name.encode('ascii','ignore').decode('ascii')
    price = soup.findAll('div',text=re.compile(r'MSRP:*'))[0].parent.parent.text
    fromp = soup.findAll('div',text=re.compile(r'From:*'))[0].parent.parent.text
    percent = soup.findAll('div',text=re.compile(r'In Stock at*'))[0]
    date = soup.findAll('a',text=re.compile(r'Added:*'))[0]

    return (name, price, fromp, percent, date)

def text_with_br(elem):
    text = ''
    for e in elem.recursiveChildGenerator():
        if isinstance(e, basestring):
            text += e.strip()
        elif e.name == 'br':
            text += '  \t'
    return text

csvfile = open('items.csv', 'wb')
writer = csv.writer(csvfile, delimiter='\t',quoting=csv.QUOTE_MINIMAL)
writer.writerow(['Walmart ID', 'Walmart address','Walmart city',"phone",'distance','price', 'OOS?','number left'])

br = Browser()

# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot

br.addheaders = [('User-agent', 'Firefox')]
idlist = []
with open('walmart_skuids.csv', 'rb') as csvfile:
    cvsreader = csv.reader(csvfile)
    for row in cvsreader:
        idlist.extend(row)
#idlist = ['9914706','43255682']
#idlist = ['15913490']
ziplist = ['11784','37203']
#ziplist = ['11784']

# fill the form
izip = 0
print 'total we have ', len(ziplist), ' zips, ', len(idlist), ' skuids'
for zipcode in ziplist:
    iskuid = 0
    izip = izip + 1
    for skuid in idlist:
        iskuid = iskuid + 1
        print 'izip = ', izip, ', iskuid = ', iskuid
        # Retrieve the Google home page, saving the response
        br.open("http://brickseek.com/walmart-inventory-checker")
        br.select_form( nr=1 )
        br.form[ 'zip' ] = zipcode
        br.form['item_id'] = skuid

        # Get the search results
        resp = br.submit()

        # parse the result
        soup = BeautifulSoup(resp)
        #soup.findAll('br').replaceWith("  \t");
        #for linebreak in soup.findAll('br'):
        #    print linebreak
            #linebreak.extract()
        #    linebreak.replaceWith('   \t')
#        soup = BeautifulSoup(str(soup).replace('<br>','  '))
        soup = BeautifulSoup(str(soup).replace('<br />','  '))
        soup = BeautifulSoup(str(soup).replace('<br/>','  '))
        soup = BeautifulSoup(str(soup).replace('<b>','  '))
        #soup = BeautifulSoup(str(soup).replace('</b>','  '))
        soup = BeautifulSoup(str(soup).replace('</a>','  '))
        soup = BeautifulSoup(str(soup).replace('$    ', '$'))
        soup = BeautifulSoup(str(soup).replace('Out of Stock', '|  Out of Stock'))
        soup = BeautifulSoup(str(soup).replace('In Stock', '|  In Stock'))
        #titleTag = soup.html.head.title
        #writer.writerow(list(titleTag))
        writer.writerow([])
        name, price, fromp, percent, date = findname(skuid)
        writer.writerow(['zipcode ='+zipcode, 'skuid = '+skuid, name, price, fromp, percent, date])
        table = soup('table')[0]
        #name = table.find_previous_sibling()
        #print name.text
        for row in table.findAll('tr'):
            tds = row('td')
            #row = [text_with_br(elem) for elem in tds]
            row = [elem.text for elem in tds if not elem.text.startswith('stock')]
            if len(row) <= 1:
                continue
            #row = [elem.replace('$     ','$') for elem in row]
            writer.writerow(row)
        #for row in soup.find_all('tr'):
        #    print '\n'.join(row.stripped_strings)
        #print resp.read()
