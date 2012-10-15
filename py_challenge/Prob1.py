__author__ = 'eolander'

text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def xlate(x):
    if x < 'a' or x > 'z':
        return x
    else:
        return chr((ord(x) + 2 - ord('a')) % 26 + ord('a'))

print ''.join(map(xlate, text))

# http://www.pythonchallenge.com/pc/def/ocr.html
