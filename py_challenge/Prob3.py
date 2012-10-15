__author__ = 'eolander'

import re

text = ''.join([line.rstrip('\n') for line in open('Prob3.txt')])

#print text

#pattern = ".*[a-z]([A-Z]{3}[a-z][A-Z]{3})[a-z].*"

pattern = "[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]"

print ''.join(re.findall(pattern, text))

#http://www.pythonchallenge.com/pc/def/linkedlist.html