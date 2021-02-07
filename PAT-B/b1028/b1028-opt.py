"""
    @name     : b1028
    @version  : 21.0207
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : all
    @desc     : p3考虑无有效生日，p4易超时
"""

import sys

today = '2014/09/06'
oldest = '1814/09/06'

count = int(input())
lines = sys.stdin.readlines()
valid = filter(lambda y: oldest <= y[1] <= today, map(lambda x: x.split(), lines))
valid = sorted(valid, key=lambda x:x[1])

if len(valid):
    print(len(valid), valid[0][0], valid[-1][0])
else:
    print(0)
