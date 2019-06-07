import pandas as pd
df = pd.read_csv('pydata-book/ch06/ex1.csv')
df
pd.read_table('pydata-book/ch06/ex1.csv',sep=',')
pd.read_csv('pydata-book/ch06/ex2.csv',header=None)
pd.read_csv('pydata-book/ch06/ex2.csv',names=['a','b','c','d','message'])
names=['a','b','c','d','message']
pd.read_csv('pydata-book/ch06/ex2.csv',names=names,index_col='message')
parsed=pd.read_csv('pydata-book/ch06/csv_mindex.csv',index_col=['key1','key2'])
parsed
list(open('pydata-book/ch06/ex3.txt'))
list(open('pydata-book/ch06/ex3.dat'))
list(open('pydata-book/ch06/ex3.csv'))
result = pd.read_table('pydata-book/ch06/ex3.csv',sep='\s+')
result
pd.read_csv('pydata-book/ch06/ex4.csv',skiprows=[0, 2, 3])
result = pd.read_csv('pydata-book/ch06/ex5.csv')
result
pd.isnull(result)
result = pd.read_csv('pydata-book/ch06/ex5.csv',na_values=['NULL'])
result
setinels = {'message':['foo','NA'],'something':['two']}
pd.read_csv('pydata-book/ch06/ex5.csv',na_values=setinels)
result = pd.read_csv('pydata-book/ch06/ex6.csv')
result
result = pd.read_csv('pydata-book/ch06/ex6.csv',nrow=5)
result = pd.read_csv('pydata-book/ch06/ex6.csv',nrows=5)
result
result = pd.read_csv('pydata-book/ch06/ex6.csv',chunksize=5)
result = pd.read_csv('pydata-book/ch06/ex6.csv',chunksize=1000)
chunker
result
tot = Series([])
tot = pd.Series([])
for piece in result:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.order(ascending=False)
tot = tot.sort_values(ascending=False)
tot[:10]
tot
data = pd.read_csv('pydata-book/ch06/ex5.csv')
data
data.to_csv('pydata-book/ch06/out.csv')
!cat pydata-book/ch06/out.csv
data.to_csv(sys.stdout,sep='|')
data.to_csv(sys.stdout,na_rep='NULL')
data.to_csv(sys.stdout,index=False,cols=['a','b','c'])
data.to_csv(sys.stdout,index=False,columns=['a','b','c'])
dates=pd.date_range('1/1/2000',periods=7)
ts=pd.Series(np.arange(7),index=dates)
ts.to_csv(sys.stdout)
ts.to_csv('pydata-book/ch06/tseries.csv')
pd.Series.from_csv('pydata-book/ch06/tseries.csv',parse_dates=True)
import csv
f = open('pydata-book/ch06/ex7.csv')
reader = cvs.reader(f)
reader = csv.reader(f)
for line in reader:
    print line
lines = list(csv.reader(open('pydata-book/ch06/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h:v for h,v in zip(header,zip(*values))}
data_dict
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
reader = csv.reader(f, dialect=my_dialect)
reader = csv.reader(f)
reader = csv.reader(f, delimiter='|')
reader
with open('mydata.csv','w') as f:
    writer  = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one','two',three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    writer.writerow(('7','8','9'))
with open('mydata.csv','w') as f:
    writer  = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    writer.writerow(('7','8','9'))
from lxml.html import parse
from urllib2 import urlopen
parsed= parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
doc = parsed.getroot()
doc
links = doc.findall('.//a')
links
links[15:20]
lnk = links[28]
lnk
lnk.get('href')
lnk.text_content()
urls = [lnk.get('href') for lnk in doc.findall('.//a')]
urls
urls[-10:]
tables = doc.findall('.//table')
calls = tables[9]
calls = tables[1]
puts= tables[13]
tables
puts= tables[2]
rows = calls.findall('.//tr')
def _unpack(row, kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text_content() for val in elts]
_unpack(rows[0], kind='th')
_unpack(rows[1], kind='td')
rows[1]
from pandas.io.parsers import TextParser
def parse_options_data(table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0],kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names = header).get_chunk()
call_data = parse_options_data(calls)
put_data = parse_options_data(puts)
call_data[:10]
put_data[:10]
from lxml import objectify
path =  'Performance_MNR.xml'
parsed = objectify.parse(open(path))
frame = pd.read_csv('pydata-book/ch06/ex1.csv')
frame
frame.save('pydata-book/ch06/frame_pickle')
import requests
url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url_
)
resp = requests.get(url)
resp
import json
data = json.loads(resp.text)
data.keys()
url = 'https://api.twitter.com/1.1/search/tweets.json?q=python%20pandas'
resp = requests.get(url)
data = json.loads(resp.text)
data.keys()
import sqlite3
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()
ls
data = [('Atlanta','Georgia',1.25,6), ('Tallahassee','Florida',2.6,3), ('Sacramento','California',1.7,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()
cursor = con.execute('select * from test')
rows=cursor.fetchall()
rows
cursor.description
DataFrame(rows,columns=zip(*cursor.description)[0])
pd.DataFrame(rows,columns=zip(*cursor.description)[0])
import pandas.io.sql as sql
sql.read_sql('select * from test',con)
import pymongo
url = 'https://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
data = json.loads(resp.text)
data.keys()
%history -f pythonio.py
