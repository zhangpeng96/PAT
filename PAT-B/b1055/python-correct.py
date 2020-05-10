
n, k = map(int,input().split())
lst = []
for i in range(n):
    name, height = input().split()
    lst.append([int(height), name])
 
lst.sort(key=lambda x:(-x[0], x[1]))
n_per_row = n//k
n_lastrow = n - n_per_row * (k-1)
person_eachrow = [lst[:n_lastrow]] + [ lst[n_lastrow + n_per_row * i:n_lastrow + n_per_row * (i+1)]  for i in range(k-1)]
# print(person_eachrow)

for pers in person_eachrow:
    length = len(pers)
    ret = ['' for i in range(length)]
    mid = length//2
    ret[mid] = pers[0][1]
    cn = 1
    for j in range(1,length,2):
        if j == length - 1:
            ret[mid - cn] = pers[j][1]
        else:
            ret[mid - cn] = pers[j][1]
            ret[mid + cn] = pers[j+1][1]
            cn += 1
    print(" ".join(ret))
 

'''


0 1 2 3 4 5 6

1 3 5 6 4 2 0
[i for i in range(1, 7, 2)] + [i-1 for i in range(7, 0, -2)]


0 1 2 3 4 5 6 7

7 ->
  2 4 6 7 5 3 1

0 2 4 6 7 5 3 1


[0] + [i for i in range(2, 8, 2)] + [i-1 for i in range(8, 0, -2)]
'''
