__author__ = 'eolander'

text = ''.join([line.rstrip('\n') for line in open('Prob2.txt')])

def counts(l, acc):
    if not l:
        return acc
    else:
        acc.append((l[0], l.count(l[0])))
        return counts(filter(lambda(x): x != l[0], l), acc)

print counts(list(text), [])

#http://www.pythonchallenge.com/pc/def/equality.html
