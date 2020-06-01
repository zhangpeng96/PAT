'''
    @name      : a1041
    @version   : 20.0601
    @author    : zhangpeng96
    @test_time : 16'37"
    @pass_rate : all
'''

from collections import Counter

# ins = '7 5 31 5 88 67 88 17'
# ins = '5 888 666 666 888 888'
digits = input().split()[1:]
unique = set()

def search(digits, unique):
    for digit in digits:
        if digit in unique:
            return digit
    return 'None'

for digit, times in Counter(digits).most_common()[::-1]:
    if times != 1:
        break
    unique.add(digit)

print(search(digits, unique))

'''
    注意在添加字典元素时区分 add 和 update 方法，add 为添加单个元素，
    因此添加字符串时不会将字符串分割为字符
'''
