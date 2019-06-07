import re
with open('regex_sum_207733.txt') as f:
    sum = 0
    for line in f:
        num = re.findall('[0-9]+',line)
        for i in num:
            sum = sum + int(i)
    print sum

