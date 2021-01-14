"""
    @name      : a1015
    @version   : 21.0114
    @author    : zhangpeng96
    @test_time : 23'00"
    @pass_rate : all
"""

from math import sqrt

def prime(n):
    if n == 1: return False
    for p in range(2, int(sqrt(n))+1):
        if not n % p:
            return False
    return True

def radix(n, base):
    if n < base:
        return str(n)
    else:
        return radix(n//base, base) + str(n % base)

def judge(digit, d):
    if prime(digit):
        rev = radix(digit, d)[::-1]
        if prime(int(rev, d)):
            return True
    return False

# print(int('2475', 8)) # radix -> decimal

while True:
    ins = input().split()
    if int(ins[0]) < 0:
        break
    elif len(ins) == 2:
        if judge(int(ins[0]), int(ins[1])):
            print('Yes')
        else:
            print('No')
