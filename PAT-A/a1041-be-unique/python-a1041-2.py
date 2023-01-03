'''
    @name      : a1041
    @version   : 20.0601.3
    @author    : zhangpeng96
    @test_time : 
    @pass_rate : p4, p5 timeout
'''


# ins = '7 5 31 5 88 67 88 17'
# ins = '5 888 666 666 888 888'
# digits = ins.split()[1:]
digits = input().split()[1:]
repeat = set()

def search(digits):
    for digit in digits:
        if digit not in repeat:
            if digits.count(digit) == 1:
                return digit
            else:
                repeat.add(digit)
    return 'None'

print(search(digits))
