"""
    @name     : a1029
    @version  : 21.0222
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : all
    @source   : https://blog.csdn.net/qq_40941722/article/details/104275304
"""

from math import inf

length1, *s1 = map(int, input().split())
length2, *s2 = map(int, input().split())
s1.append(inf)
s2.append(inf)

pos, mid = 0, (length1 + length2 - 1)//2
p, q = 0, 0

while pos < mid:
    if s1[p] < s2[q]:
        p += 1
    else:
        q += 1
    pos += 1

if s1[p] < s2[q]:
    print(s1[p])
else:
    print(s2[q])
