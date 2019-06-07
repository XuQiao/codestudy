def log(text=''):
#def logfunc):
    def decorater(func):
        def wrapper(*args, **kw):
            print('%s, %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorater

#now=log(now,text='exec')
#@log('execute')
@log()
def now():
    print('2')
    pass

now()


