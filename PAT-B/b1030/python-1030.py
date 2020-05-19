'''
    @name      : b1030
    @version   : 20.0519
    @author    : zhangpeng96
    @test_time : 27'44"
    @pass_rate : 
'''

def seq_counter(sorted_tuple, mp):
    count = 0
    for digit in sorted_tuple:
        if digit <= mp:
            count += 1
        else:
            return count
    return 0

# count, p = tuple(map(int, input().split()))
# digits = tuple(sorted(map(int, input().split())))

count, p = tuple(map(int, '10 1'.split()))
digits = tuple(sorted(map(int, '1 1 1 1 9 8'.split())))

combination = [seq_counter(digits[i:], digits[i]*p) for i in range(len(digits))]
print(max(combination))
