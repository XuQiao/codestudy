ab = {
        'Swroop':'S@g.com',
        'Swroop1':'S1@g.com',
        'Swroop2':'S2@g.com',
        'Swroop3':'S3@g.com'
        }
namesp = 'Swroop3'
print ('%s email is %s' %(namesp,ab[namesp]))
ab['Swroop4'] = 'S4@g.com'
del ab['Swroop2']
print ('lens of the dict is %d' %len(ab))
for name,address in ab.items():
    print ('Contact %s as %s' %(name,address))

if 'Swroop1' in ab:
    print ('S2\'s email address is %s' %ab['Swroop1'])

