import os.path, time
import re
import sys

def main():

    inputpath = '/home/xuq7/codestudy/python/FileInventory/'
    webpath = '/home/xuq7/web/'
    counter = sys.argv[1] 

    dir1 = dict()
    dir2 = dict()
    dir3 = dict()

    with open(inputpath + 'store.inv1.' + counter) as input1:
        lines_dir1 = input1.read().splitlines()
 	dir1[0] = parseDu(lines_dir1)

    with open(inputpath + 'store.inv2.' + counter) as input2:
        lines_dir2 = input2.read().splitlines()
	dir2[0] = parseLioDu(lines_dir2)

    with open(inputpath + 'store.inv3.' + counter) as input3:
        lines_dir3 = input3.read().splitlines()
        dir3[0] = parseDu(lines_dir3)

    prevDays = (1,3,7)

    for age in prevDays:

      if os.path.isfile(inputpath + 'store.inv1.' + str(int(counter)-age)):
          with open( inputpath + 'store.inv1.' + str(int(counter)-age) ) as old_dir1:
              lines_dir1 = old_dir1.read().splitlines()    
          dir1[age] = parseDu(lines_dir1)
          loadOldSize(dir1[0],dir1[age],age)
          loadOldCount(dir1[0],dir1[age],age)

      if os.path.isfile(inputpath + 'store.inv2.' + str(int(counter)-age)):
          with open( inputpath + 'store.inv2.' + str(int(counter)-age) ) as old_dir2:
              lines_dir2 = old_dir2.read().splitlines()    
          dir2[age] = parseLioDu(lines_dir2)
          loadOldSize(dir2[0],dir2[age],age)
          loadOldCount(dir2[0],dir2[age],age)

      if os.path.isfile(inputpath + 'store.inv3.' + str(int(counter)-age)):
          with open( inputpath + 'store.inv3.' + str(int(counter)-age) ) as old_dir3:
              lines_dir2 = old_dir2.read().splitlines()
          dir3[age] = parseLioDu(lines_dir2)
          loadOldSize(dir3[0],dir3[age],age)
          loadOldCount(dir3[0],dir3[age],age)
       

    constructStatusPage(dir1[0],dir2[0],dir3[0],webpath+'fileInventory.html',prevDays)

class T2Directory:
    def __init__(self,name,count,size):
        self.name = name
        self.count = count
        self.size = size
        self.oldsize = dict()
        self.oldcount = dict()
    def printHTMLTable(self,file,totalsize,totalcount,prevDays):
	if self.size < 1000**1:
          sizestr = str( round( self.size,2 ) )
	  unit = "B"
	elif(self.size >= 1000**1 and self.size < 1000**2):
          sizestr = str( round( self.size / 1000**1,2 ) )
	  unit = "K"
	elif(self.size >= 1000**2 and self.size < 1000**3):
          sizestr = str( round( self.size / 1000**2,2 ) )
	  unit = "M"
	elif(self.size >= 1000**3 and self.size < 1000**4):
          sizestr = str( round( self.size / 1000**3,2 ) )
	  unit = "G"
	else:
          sizestr = str( round( self.size / 1000**4,2 ) )
	  unit = "T"
        sizepercent = str( round( self.size / totalsize * 100,2 ) )
        countpercent = str( round( float(self.count) / float(totalcount) * 100,2 ) )
        truncname = (self.name[:15] + '...') if len(self.name) > 18 else self.name
        if self.name == 'TOTAL':
          file.write('<tr style="font-weight:bold;"><td>' + truncname + '</td>')
        else:
          file.write('<tr><td>' + truncname + '</td>')
        file.write('<td>&nbsp;</td>\n')
        file.write('<td>' + sizestr + unit + '</td>\n')
        if self.name == 'TOTAL':
          file.write('<td>N/A</td>')
        else:
          file.write('<td><div style="float:left; width:55%; background: #FFFFFF; border: 1px solid black;')
          file.write('padding:2px;">')
          file.write('<div style="width:'+sizepercent+'%; background: #000000;">&nbsp;</div>\n')
          file.write('</div>&nbsp;'+sizepercent+'%</td>\n')
        for age in prevDays:
          if age in self.oldsize:
            if int(self.oldsize[age]) < int(self.size) :
              file.write('<td style="color:blue;">+')
            if int(self.oldsize[age]) > int(self.size) :
              file.write('<td style="color:red;">')
            if int(self.oldsize[age]) == int(self.size) :
              file.write('<td>')
            change = str( round( (self.size-self.oldsize[age]) / 1000**2,2 ) )
            file.write(change+'M </td>\n')
          else:
            file.write('<td> N/A </td>\n')   
        file.write('<td>&nbsp;</td>\n')
        file.write('<td>' + str(self.count) + '</td>\n')
        if self.name == 'TOTAL':
          file.write('<td>N/A</td>')
        else:
          file.write('<td><div style="float:left; width:55%; background: #FFFFFF; border: 1px solid black;')
          file.write('padding:2px;">')
          file.write('<div style="width:'+countpercent+'%; background: #000000;">&nbsp;</div>\n')
          file.write('</div>&nbsp;'+countpercent+'%</td>\n')
        for age in prevDays:
          if age in self.oldcount:
            if int(self.oldcount[age]) < int(self.count) :
              file.write('<td style="color:blue;">+')
            if int(self.oldcount[age]) > int(self.count) :
              file.write('<td style="color:red;">')
            if int(self.oldcount[age]) == int(self.count) :
              file.write('<td>')
            change = str(  int(self.count)-int(self.oldcount[age]) )
            file.write(change+'</td>\n')
          else:
            file.write('<td> N/A </td>\n')   
        file.write('</tr>\n')

def loadOldSize(new, old, age ):
    for ndir in new:
        for odir in old:
            if ndir.name == odir.name:
                ndir.oldsize[age] = odir.size

def loadOldCount(new, old, age ):
    for ndir in new:
        for odir in old:
            if ndir.name == odir.name:
                ndir.oldcount[age] = odir.count

def parseLioDu(lines):
    dirs = list()
    for entry in lines:
        # skip lines not starting with a number
        if not re.match(r'^[\s]*[0-9]',entry): 
            continue
        val = entry.split()
        name = val[2].rstrip('/').split('/')[-1]
        dirs.append( T2Directory(name,val[1],IECStringToBytes(val[0])) )
        
    return dirs

def parseDu(lines):
    dirs = list()
    for entry in lines:
        # skip lines not starting with a number
        if not re.match(r'^[0-9]',entry):
            continue
        val = entry.split()
        name = val[1].rstrip('/').split('/')[-1]
        dirs.append( T2Directory(name,val[2],float(val[0])) )

    return dirs

def IECStringToBytes(string):
    val = float(re.findall(r'\d+\.\d+', string)[0])
    if( re.match(r'.*ki',string) ): val *= 1024 
    if( re.match(r'.*Mi',string) ): val *= 1024**2
    if( re.match(r'.*Gi',string) ): val *= 1024**3
    if( re.match(r'.*Ti',string) ): val *= 1024**4
    if( re.match(r'.*Pi',string) ): val *= 1024**5
    if( re.match(r'.*k$',string) ): val *= 1000 
    if( re.match(r'.*K$',string) ): val *= 1000 
    if( re.match(r'.*M$',string) ): val *= 1000**2
    if( re.match(r'.*G$',string) ): val *= 1000**3
    if( re.match(r'.*T$',string) ): val *= 1000**4
    if( re.match(r'.*P$',string) ): val *= 1000**5
    return val

def printFileInventory(dirs):

    dirs.sort(key=lambda x: x.size,reverse=True)
    for item in dirs:
        sizestr = str( round( item.size / 1000**2, 2 )  )
        print item.name + "\t" + sizestr + "M" 

def constructStatusPage(dir1,dir2,dir3,outfile,prevDays):

    dir1.sort(key=lambda x: x.size,reverse=True)
    dir2.sort(key=lambda x: x.size,reverse=True)

    html = open(outfile,'w')
    
    html.write('<html>\n')
    html.write('<head>\n')
    html.write('<title>T2 Vanderbilt Storage Inventory</title>\n')
    html.write('<meta http-equiv="refresh" content="7200">\n')
    html.write('<style>table, th, td {border: 1px solid black; padding: 0.4em; }')
    html.write('table { border-collapse: collapse; } </style>')
    html.write('</head>\n')
    
    html.write('<body>\n')

    html.write("Inventory performed at: %s<br />\n" % time.ctime(os.path.getmtime('store.inv1.' + sys.argv[1])))
    html.write('Page generated at: '+str(time.ctime())+'<br /><br />\n')

    #html.write('<div style="float:left;width:48%">\n')
    html.write('<div>\n')
    html.write('<h2>/home/xuq7 Inventory</h2><br />\n')
#    html.write('<h3>Total File Size: ' + str(round(dir1[0].size/1000**4,2)) + 'T ' )
#    html.write('&emsp;&emsp;&emsp;')
#    html.write('Total File Count: '+str(dir1[0].count)+'</h3><br />\n')
    html.write('<table>')
    html.write('<tr><td><b>Directory</b></td>')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>Size</b></td>')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>File Count</b></td>\n')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('</tr>')
    for item in dir1:
        #if item.name == 'TOTAL':
        #    continue
        item.printHTMLTable(html,dir1[0].size,dir1[0].count,prevDays)
    html.write('</table></div>\n')

    html.write('<div>\n')
    html.write('<h2>/store/user/qixu Inventory</h2><br />\n')
#    html.write('<h3>Total File Size: ' + str(round(dir2[0].size/1000**4,2)) + 'T ' )
#    html.write('&emsp;&emsp;&emsp;')
#    html.write('Total File Count:'+str(dir2[0].count)+'</h3><br />\n')
    html.write('<table>')
    html.write('<tr><td><b>Directory</b></td>')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>Size</b></td>')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>File Count</b></td>\n')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('</tr>')
    for item in dir2:
        #if item.name == 'TOTAL':
        #    continue
        item.printHTMLTable(html,dir2[0].size,dir2[0].count,prevDays)
    html.write('</table>\n')

    html.write('<div>\n')
    html.write('<h2>/scratch/xuq7 Inventory</h2><br />\n')
    html.write('<table>')
    html.write('<tr><td><b>Directory</b></td>')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>Size</b></td>')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('<td>&nbsp;</td>')
    html.write('<td><b>File Count</b></td>\n')
    html.write('<td style="width:200px;"><b>Percent of Total</b></td>\n')
    for age in prevDays:
      html.write('<td><b>'+str(age)+' Day Change</b></td>\n')
    html.write('</tr>')
    for item in dir3:
        #if item.name == 'TOTAL':
        #    continue
        item.printHTMLTable(html,dir3[0].size,dir3[0].count,prevDays)
    html.write('</table>\n')

    html.write('</body></html>\n')
             
    html.close()


main()
