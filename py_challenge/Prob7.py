import urllib

__author__ = 'eolander'

import png
import Image
import ImageFilter

#r=png.Reader(file=urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png'))
#print r
#i = r.read()
#print i
#print r.color_planes
#print r.preamble()
#image = png.open('oxygen.png')
#print image.info
#print image.histogram()
#print image.getcolors()
#image.show()
image = Image.open('oxygen.png')

#image.filter(ImageFilter.SHARPEN).show()
#image.filter(ImageFilter.DETAIL).show()
print image.info
print image.mode
print image.format
print image.size
bar = image.crop((0,43,608, 43+9))
print bar.getcolors()
bar.show()
print bar.getpixel((0,0))
incr = 5
pos = 0
while pos < 608:
    print chr(bar.getpixel((pos, 0))[0]),
    pos = pos + incr
    incr = 7

print map(chr, [105 ,  110 ,   116 ,   101 ,   103 ,   114 ,   105 ,   116 ,   121 ])
#print image.transparency
#red, green, blue, alpha = image.split()
#red.show()
#alphaData = image.tostring("raw", "A")

#ai = Image.fromstring("L", image.size, alphaData)
#ai.show()

#http://www.pythonchallenge.com/pc/def/integrity.html