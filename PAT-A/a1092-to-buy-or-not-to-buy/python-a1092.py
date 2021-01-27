"""
    @name     : a1092
    @version  : 21.0127
    @author   : zhangpeng96
    @time     : 12'00"
    @accepted : all
"""

from collections import Counter

given = input()
wanted = input()
surplus = len(given)-len(wanted)
sub = Counter(wanted) - Counter(given)

if sub:
    miss = sum(map(lambda x:x[1], sub.most_common()))
    print('No {}'.format(miss))
else:
    print('Yes {}'.format(surplus))
