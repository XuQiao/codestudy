#!/usr/bin/python

try:
    text = input('Enter something -->')
except EOFError:
    print('EOF error!')
except KeyboardInterrupt:
    print('Operating cancelled!')
else:
    print('You entered {0}'.format(text))
