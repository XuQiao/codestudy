#!/usr/bin/python

import pickle

shoplistfile = 'shoplist.dat'
shoplist = ['apple','mango','carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()
