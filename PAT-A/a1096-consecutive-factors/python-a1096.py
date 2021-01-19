from math import sqrt

# number = int('630')
number = int(input())
max_n = int(sqrt(number)) + 1
factors = []
result = []

for a in range(2, max_n):
    product = 1
    for b in range(a, max_n):
        product *= b
        print(a, b, product)
        if number % product:
            break
        else:
            length = b-a+1
            if product*length == number:
                result.append((length, a, b))

if len(result):
    length, start, end = sorted(result, key=lambda x: (-x[0], x[1]))[0]
    print(length)
    print('*'.join(map(str, [i for i in range(start, end+1) ])))
else:
    print('1\n{}'.format(number))