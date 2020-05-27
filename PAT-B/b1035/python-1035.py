# 20'16"
count = int('10')
digits = list(map(int, '3 1 2 8 7 5 9 4 6 0'.split()))
sorts = '1 2 3 7 8 5 9 4 6 0'
# sorts = list(map(int, '1 2 3 7 8 5 9 4 6 0'.split()))

interme = []
for i in range(count-1):
    interme += [ digits[i] ]
    insert_str = ' '.join(map(str, sorted(interme) + digits[i+1:]))
    if insert_str == sorts:
        print(i)
        break

