import sys
tank, distance, per, count = map(int,input().split())
b = sorted([list(map(eval,input().split())) for i in range(count)],\
           key = lambda x: x[1]) + [[-1,distance],[float('inf'),0]]
if b[0][1] != 0:
    print('The maximum travel distance = 0.00')
    sys.exit(0)
i,m,n = 0,b[0] + [0],[]
while i < count:
    j,q = i + 1,count + 1
    while b[j][1] - m[1] <= tank * per:
        if b[j][0] < m[0]:
            n.append([b[i][0],b[j][1] - sum(m[1:])])
            q = j
            break
        if b[j][0] < b[q][0]:
            q = j
        j += 1
    else:
        if b[q][1]:
            n.append([b[i][0],tank * per - m[2]])
        else:
            print('The maximum travel distance = {:.2f}'.format(m[1] + tank * per))
            break
    i,m = q,b[q] + [sum(m[1:]) + n[-1][1] - b[q][1]]
else:
    print('{:.2f}'.format(sum([i[0] * i[1] for i in n]) / per))
