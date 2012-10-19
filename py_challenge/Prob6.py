__author__ = 'eolander'

import zipfile
import re

nothing='90052'
pattern = 'Next nothing is ([0-9]+)'
ctr = 0

print zipfile.ZipInfo('channel.zip').comment

with zipfile.ZipFile('channel.zip', 'r') as myzip:
    print myzip.comment.__len__()
    while nothing:
        nothing = re.search(pattern, myzip.open(nothing+'.txt').read()).group(1)
        print myzip.getinfo((nothing+'.txt')).comment,
       # print ctr, nothing
       # ctr = ctr + 1

#http://www.pythonchallenge.com/pc/def/oxygen.html