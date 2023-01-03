'''
    @name      : b1053
    @version   : 20.0519
    @author    : zhangpeng96
    @test_time : 28'02"
    @pass_rate : all
'''

from collections import Counter

def pre_vacancy(records, threshold):
    if len(tuple(filter(lambda r: r < threshold, records))) > len(records) // 2:
        return True
    else:
        return False

def act_vacancy(records, threshold, days):
    if pre_vacancy(records, threshold):
        if len(records) > days:
            return 'a'
        else:
            return 'p'


# count, threshold, days = tuple('5 0.5 10'.split())
# records = ['6 0.3 0.4 0.5 0.2 0.8 0.6','10 0.0 0.1 0.2 0.3 0.0 0.8 0.6 0.7 0.0 0.5','5 0.4 0.3 0.5 0.1 0.7','11 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1','11 2 2 2 1 1 0.1 1 0.1 0.1 0.1 0.1']

count, threshold, days = tuple(input().split())
count, threshold, days = int(count), float(threshold), int(days)

records = [input() for _ in range(count)]

records = map(lambda x: tuple(map(float, x.split()[1:])), records)
counter = Counter(map(lambda r: act_vacancy(r, threshold, days), records))

print('{:.1%} {:.1%}'.format(counter['p'] / count, counter['a'] / count))
