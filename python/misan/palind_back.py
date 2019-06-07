def  find_palindromes(year): # 1000 <= year <= 9999
    ndates = 0 # number of dates
    century = year - year % 100 # only the century matter for the input
    list = []
    for y in range(century, century + 100): # scan over 100 years for that Century
        if num_palind(y) != 0:
            list.append((y, num_palind(y)))
        ndates += num_palind(y) # accumlate palindromes dates in a year
    print ndates
    print list
    return ndates

def num_palind(year):
    y1 = year / 1000 # first digit
    y2 = (year % 1000) / 100 # second digit
    y3 = (year % 100) / 10 # third digit
    y4 = (year % 10) / 1 # fourth digit
    palind_date_7 = 0 # if it is a 7 digit palind date
    palind_date_8 = 0 # if it is a 8 digit palind date
    # Seven digits m d1 d2 y1 y2 y3 y4, m = y4, d1 d2 = y3 y2
    date = y3 * 10 + y2 # the date number
    if valid_date(y4, date, year): # has to be valid given month
        palind_date_7 = 1
#    if valid_date(y4*10+y3, y2):
#        palind_date_7 += 1
    
    #Eight digits m1 m2 d1 d2 y1 y2 y3 y4, m1 m2 = y4 y3, d1 d2 = y2 y1
    month = y4 * 10 + y3
    date = y2 * 10 + y1
    if valid_date(month, date, year):
        palind_date_8 = 1
    
    return palind_date_7 + palind_date_8 # return the number of palind dates in this year

def valid_date(month, date, year):
    if date == 0 or month == 0 or month > 12:
        return False
    if (month in [1, 3, 5, 7, 8, 10, 12] and date > 31): # longer month
        return False
    if (month in [4, 6, 9, 11] and date > 30): # shorter month
        return False
    if (month == 2 and year % 4 == 0 and date > 29): # cannot be 2/29 because the last digit of year needs to be '00'
        return False
    if (month == 2 and year % 4 != 0 and date > 28): # cannot be 2/29 because the last digit of year needs to be '00'
        return False
    
    return True

find_palindromes(1000)
find_palindromes(2016)
find_palindromes(2139)
find_palindromes(8201)
find_palindromes(2901)
