from time import time


def decorater(func):
    def t(*p):
        s = time()
        y = func(*p)
        d = time()
        return d - s

    return t


@decorater
def liste(q):
    e = input('pleas enter paired or unpaired or prime numbers: ').lower()
    for r in q:
        if e == 'paired':
            if r % 2 == 0:
                return r
        if e == 'prime':
            if r % 2 != 0 and r % 3 != 0 and r % 5 != 0 and r % 7 != 0 or r == 2 or r == 3 or r == 5 or r == 7:
                return r
        if e == 'unpaired':
            if r % 2 == 1:
                return r


print(liste(list(range(1, 10000000))))
