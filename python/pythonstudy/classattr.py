class Chain(object):
    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
#           return lambda user: Chain('%s/%s/:%s' % (self._path, path, user))
            def setuser(user):
                return Chain('%s/%s/:%s' % (self._path, path, user))
            return setuser
        return Chain('%s/%s' % (self._path, path))


    def __str__(self):
        return self._path

    __repr__ = __str__



print (Chain().status.user.timeline.list)
print (Chain().users('michael').repos)
