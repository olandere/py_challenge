__author__ = 'eolander'
import re
import urllib

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#nothing = '12345'
nothing='8022'
pattern = 'and the next nothing is ([0-9]+)'

for x in range(400):
    page = urllib.urlopen(baseurl+nothing).read()
    nothing = re.search(pattern, page).group(1)
    print(x, nothing)

#http://www.pythonchallenge.com/pc/def/peak.html