"""
    @name     : 7-1
    @version  : 21.0209
    @author   : zhangpeng96
    @time     : 11'48"
    @accepted : all
"""

number, k = map(int, input().split())
# number, k = map(int, '12345 2'.split())

a = number
number = str(number)
index = len(number)-k
b = int( number[index:] + number[:index] )

print('{:.2f}'.format(b/a))
