"""
    @name     : a1024
    @version  : 21.0202
    @author   : zhangpeng96
    @time     : 18'00"
    @accepted : all
    @desc     : p2考虑个位数，p3考虑本身是回文数
"""

def judge(digit):
    digit = str(digit)
    i = 0
    while i < len(digit)//2:
        if not digit[i] == digit[-(i+1)]:
            return False
        i += 1
    return True

def loop(number, count):
    if judge(number):
        return number, 0
    if number < 10:
        return number, 0
    for i in range(count):
        new = number + int(str(number)[::-1])
        if judge(new):
            return new, i+1
        else:
            number = new
    return new, i+1


number, count = map(int, input().split())
print('{} {}'.format(*loop(number, count)))
