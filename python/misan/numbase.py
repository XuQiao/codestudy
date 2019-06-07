def numbase(base, number):
    b = int(base)
    if b < 2 or b > 36:
        return 'base invalid'
    result = 0
    for c in number:
        n = lettertonum(c)
        if n >= b:
            return 'number invalid'
        result = result * b + n
    return str(result)

def lettertonum(c):
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
        return int(c)
    else:
        return ord(c) - ord('a') + 10

if __name__ == '__main__':
    numbase('1','1010')
    numbase('8','19')
    numbase('2','1010')
    numbase('11','a1')
    numbase('12','c33')
    numbase('3','10101010101010')
