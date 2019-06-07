import re
def match(s):
    result = re.match(r'^([a-zA-Z0-9\_\.]+)\@([a-zA-Z0-9\_]+.com$)',s)
    return result

result = match('someone@gmail.com')
result = match('bill.gates@microsoft.com')
result = match('bill.gates microsoft.com')
#result = match('qiao.xu@vanderbilt.com')
if(result!=None):
    print ('It is an email address, name = %s' %result.group(1))
else:
    print ('It is not an email address')
