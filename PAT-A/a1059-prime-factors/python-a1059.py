"""
    @name     : a1059
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 41'32"
    @accepted : all
"""

from math import sqrt

def square(n):
    return int(sqrt(n))+1

def prime(n):
    if n == 1: return False
    if not n % 2: return n == 2
    if not n % 3: return n == 3
    if not n % 5: return n == 5
    for p in range(7, square(n), 2):
        if not n % p: return False
    return True

def formatter(d):
    p = []
    for base, exp in d.items():
        if exp > 1:
            p.append( '{}^{}'.format(base, exp) )
        else:
            p.append( '{}'.format(base) )
    return '*'.join(p)

number = int(input())
numbers = number
factors = {}

if number == 1:
    factors[1] = 1

elif prime(number):
    factors[number] = 1

else:
    prime_table = filter(prime, range(2, number+1))
    # for _ in range(square(number)):
    while number > 1:
        fact = next(prime_table)
        while not number % fact:
            number = number // fact
            factors[fact] = factors.get(fact, 0) + 1

print(factors)
print('{}={}'.format(numbers, formatter(factors)))
