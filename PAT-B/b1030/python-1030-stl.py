"""
    @name      : b1030
    @version   : 21.0105
    @author    : zhangpeng96
    @pass_rate : p4 timeout
"""

from bisect import bisect_right

ans = []
count, p = map(int, input().split())
digits = sorted(map(int, input().split()))
# count, p = map(int, '10 8'.split())
# digits = sorted(map(int, '2 3 20 4 5 1 6 7 8 9'.split()))
digits.sort()

for i, digit in enumerate(digits):
    ans.append(bisect_right(digits, digit*p, i)-i)

print(max(ans))