__author__ = 'eolander'

def head(str):
    return str[:1]

def tail(str):
    return str[1:]

def nextHelper(x, xs, acc):
    if len(xs) == 0:
        return (acc, xs)
    if x == head(xs):
        return nextHelper(x, tail(xs), acc+1)
    else:
        return (acc, xs)

def next(st):
    if len(st) == 0:
        return ''
    if len(st) == 1:
        return '1'+st
    else:
        acc, xs = nextHelper(head(st), tail(st), 1)
        return str(acc) + head(st) + next(xs)

s = '1'
for x in range(0, 30):
    print s
    s = next(s)
