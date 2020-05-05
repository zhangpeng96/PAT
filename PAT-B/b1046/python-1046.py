'''
    @name      : b1046
    @version   : 20.506
    @author    : zhangpeng96
    @test_time : 9'24"
    @pass_rate : all
'''

# input_count = int(input())
# input_list = [input() for _ in range(0, input_count)]
input_list = ['8 10 9 12','5 10 5 10','3 8 5 12','12 18 1 13','4 16 12 15']
drink_a = 0
drink_b = 0

for race in input_list:
    call_a, hand_a, call_b, hand_b = tuple(map(int, race.split()))
    call = call_a + call_b
    if hand_a == call and hand_b == call:
        pass
    elif hand_a == call:
        drink_b += 1
    elif hand_b == call:
        drink_a += 1

print(drink_a, drink_b)
