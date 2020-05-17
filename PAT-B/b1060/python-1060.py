'''
    @name      : b1060
    @version   : 20.0517
    @author    : zhangpeng96
    @test_time : 50'00"
    @pass_rate : p3 timeout
'''

# input_str = '6 7 6 9 3 10 8 2 7 8'
# input_str = '0'
# input_str = '5 5 5 5 5'

count = int(input())
input_str = input()

numbers = list(map(int, input_str.split()))

start, end = min(numbers) - 1, max(numbers) + 1

data = filter(lambda i: len(list( filter( lambda x: x > i, numbers) )) >= i, range(start, end))

print(max(data))

