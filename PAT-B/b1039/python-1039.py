'''
    @name      : b1039
    @version   : 20.0510
    @author    : zhangpeng96
    @test_time : 12'05"
    @pass_rate : all
'''

from collections import Counter

# lace_given = 'ppRYYGrrYBR2258'
# lace_wanted = 'YrR8RrY'

# lace_given = 'ppRYYGrrYB225'
# lace_wanted = 'YrR8RrY'

lace_given = input()
lace_wanted = input()

lace_sub = Counter(lace_wanted) - Counter(lace_given)

if lace_sub:
    miss_count = sum(map(lambda x:x[1], lace_sub.most_common()))
    print('No {}'.format(miss_count))
else:
    print('Yes {}'.format(len(lace_given) - len(lace_wanted)))
