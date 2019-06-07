# palindrome Dates, check how many palindrome dates in 21st Century
#!/bin/python3

import sys
import os

def find_palindromes(year): #1000 < year < 9999
    result = 0
    century = year - year % 100
    for y in range(century, century + 100):
        result += num_pand(y)
    print(result)
    return result

def num_pand(year):
    y1 = year / 1000
    y2 = (year % 1000) / 100
    y3 = (year % 100) / 10
    y4 = (year % 10) / 1
    result_7 = 0
    result_8 = 0
    #Seven digits m d d y1 y2 y3 y4
    date = y3 * 10 + y2
    if(valid_date(y4, date)):
        result_7 = 1
    
    #Eight digits m m d d y1 y2 y3 y4
    month = y4 * 10 + y3
    date = y2 * 10 + y1
    if (month >= 10 and month <= 12 and valid_date(month, date)):
        result_8 = 1
    return result_7 + result_8

def valid_date(month, date):
    if month == 0 or \
    (month in [1, 3, 5, 7, 8, 10, 12] and date > 31) \
    or (month in [4, 6, 9, 11] and date > 30) \
    or (month == 2 and date > 28):
        return False
    else:
        return True

if __name__ == '__main__':
    find_palindromes(2016)
    find_palindromes(2023)
    find_palindromes(1034)
    find_palindromes(9999)
    find_palindromes(1390)

