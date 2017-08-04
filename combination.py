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
    intN = int(n)
    intR = int(r)
    
    if(intN - intR == 0):
        c = 1
    elif(intR == 1):
        c = intN
    else:
        n1 = factorial(intN-1)
        r1 = factorial(intR)
        r2 = factorial(intN-intR)
        r3 = factorial(intR-1)
        c = (n1 / (r1*r2)) + (n1 / (r3*r2))
    print((str)(c))