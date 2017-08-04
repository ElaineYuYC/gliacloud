# -*- coding: UTF-8 -*-

import sys
sys.setrecursionlimit(5000)
def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

if __name__ == '__main__':
    n = input("n = ")
    r = input("r = ")
    n1 = factorial(int(n)-1)
    r1 = factorial(int(r))
    r2 = factorial(int(n)-(int)(r))
    r3 = factorial(int(r)-1)
    c = (n1 / (r1*r2)) + (n1 / (r3*r2))
    print((str)(c))