"""
    @name     : a1011
    @version  : 21.0218
    @author   : zhangpeng96
    @time     : 22'18"
    @accepted : all
"""

from functools import reduce

odds = [ dict( zip(map(float, input().split()), ['W','T','L']) ) for _ in range(3) ]
plan = dict( [ sorted(odd.items(), reverse=True)[0] for odd in odds ] )
amount = ( reduce(lambda x,y:x*y, plan.keys()) * 0.65 - 1 ) * 2

print('{} {} {} {:.2f}'.format(*plan.values(), amount))
