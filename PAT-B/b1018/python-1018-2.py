'''

尝试失败仍然超时
'''


from sys import stdin
from collections import Counter

def decision_status(strs):
    a, b = strs.split()
    if a == b:
        return 0
    elif a == 'C' and b == 'J':
        return 1
    elif a == 'C' and b == 'B':
        return -1
    elif a == 'J' and b == 'C':
        return -1
    elif a == 'J' and b == 'B':
        return 1
    elif a == 'B' and b == 'C':
        return 1
    elif a == 'B' and b == 'J':
        return -1

def decision_gesture_a(strs):
    a, b = strs.split()
    if a == 'C' and b == 'J':
        return 'C'
    elif a == 'J' and b == 'B':
        return 'J'
    elif a == 'B' and b == 'C':
        return 'B'

def decision_gesture_b(strs):
    a, b = strs.split()
    if a == 'C' and b == 'B':
        return 'B'
    elif a == 'J' and b == 'C':
        return 'C'
    elif a == 'B' and b == 'J':
        return 'J'

count = int(input())
hand_list = [stdin.readline().strip() for _ in range(count)]
# hand_list = ['C J','J B','C B','B B','B C','C C','C B','J B','B C','J J']

print(Counter(map(decision_status, hand_list)))
print(Counter(map(decision_gesture_a, hand_list)))
print(Counter(map(decision_gesture_b, hand_list)))

# for hand in hand_list:
#     win, gest = decision(hand)
#     if win == 1:
#         status_a[1] += 1
#         status_b[-1] += 1
#         gesture_a[gest] += 1
#     elif win == -1:
#         status_a[-1] += 1
#         status_b[1] += 1
#         gesture_b[gest] += 1
#     elif win == 0:
#         status_a[0] += 1
#         status_b[0] += 1


# print(status_a[1], status_a[0], status_a[-1])
# print(status_b[1], status_b[0], status_b[-1])
# print(sorted(gesture_a.items(), key = lambda x: (-x[1], x[0]) )[0][0], sorted(gesture_b.items(), key = lambda x: (-x[1], x[0]) )[0][0])

