from math import sqrt

number = int('360')
factors = []

for n in range(1, int(sqrt(number))):
    product = n
    while product <= number:
        n += 1
        product *= n
        if product == number:
            print(n) 
