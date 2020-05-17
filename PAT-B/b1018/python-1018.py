'''
    @name      : b1018
    @version   : 20.0517
    @author    : zhangpeng96
    @test_time : 37'51"
    @pass_rate : p5 timeout
'''

def decision(strs):
    a, b = strs.split()
    if a == b:
        return 0, None
    elif a == 'C' and b == 'J':
        return 1, 'C'
    elif a == 'C' and b == 'B':
        return -1, 'B'
    elif a == 'J' and b == 'C':
        return -1, 'C'
    elif a == 'J' and b == 'B':
        return 1, 'J'
    elif a == 'B' and b == 'C':
        return 1, 'B'
    elif a == 'B' and b == 'J':
        return -1, 'J'


count = int(input())
hand_list = [input() for _ in range(count)]
# hand_list = ['C J','J B','C B','B B','B C','C C','C B','J B','B C','J J']

gesture_a = { 'C': 0, 'J': 0, 'B': 0 }
gesture_b = { 'C': 0, 'J': 0, 'B': 0 }

status_a = { 1: 0, 0: 0, -1: 0 }
status_b = { 1: 0, 0: 0, -1: 0 }

for hand in hand_list:
    win, gest = decision(hand)
    if win == 1:
        status_a[1] += 1
        status_b[-1] += 1
        gesture_a[gest] += 1
    elif win == -1:
        status_a[-1] += 1
        status_b[1] += 1
        gesture_b[gest] += 1
    elif win == 0:
        status_a[0] += 1
        status_b[0] += 1


print(status_a[1], status_a[0], status_a[-1])
print(status_b[1], status_b[0], status_b[-1])
print(sorted(gesture_a.items(), key = lambda x: (-x[1], x[0]) )[0][0], sorted(gesture_b.items(), key = lambda x: (-x[1], x[0]) )[0][0])


'''
    The following can also pass test

print('{} {} {}'.format(*status_a.values()))
'''