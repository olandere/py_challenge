__author__ = 'eolander'

import pickle

obj = pickle.load(open('banner.p'))

print obj

for x in obj:
    for y in x:
        for z in range(y[1]):
            print y[0],
    print

#http://www.pythonchallenge.com/pc/def/channel.html


