"""
    @name     : a1044
    @version  : 21.0302
    @author   : zhangpeng96
    @time     : 58'22"
    @accepted : p2,p3,p5 timeout
  3   2   1   5   4   6   8   7  16  10  15  11   9  12  14  13
  3   5   6  11  15  21  29  36  52  62  77  88  97 109 123 136
"""

from itertools import accumulate
from collections import defaultdict

def binary_search(target, left, right):
    while left < right:
        mid = (left + right) //2
        if (chain[mid] - chain[left-1]) >= target:
            right = mid
        else:
            left = mid + 1
    return right


result = defaultdict(list)
count, pay = map(int, input().split())
chain = map(int, ('0 ' + input()).split())
chain = list(accumulate(chain))

for left in range(1, count+1):
    right = binary_search(pay, left, count)
    amount = chain[right] - chain[left-1]
    if amount >= pay:
        result[amount].append((left, right))

for pair in result[min(result.keys())]:
    print('{}-{}'.format(*pair))
