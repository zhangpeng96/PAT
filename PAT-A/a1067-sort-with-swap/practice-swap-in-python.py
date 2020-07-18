import time

number = [0] * 10
insert = map(int, '3 5 7 2 6 4 9 0 8 1'.split())
for i, item in enumerate(insert):
    number[item] = i

count = 0

def swap(a, b):
    temp = a
    b = a
    a = temp
    print(number)
    time.sleep(5)

for i in range(1, len(number)):
    if i != number[i]:
        while number[0] != 0:
            swap(number[0], number[ number[0] ])
            count += 1
        if i != number[i]:
            swap(number[0], number[i])
            count += 1

print(count)




