'''
source: https://blog.csdn.net/qq_41398808/article/details/83549933
'''

n = int(input())
partner = []
for i in range(n):
    partner.append(input().split())
m = int(input())
singal = input().split()
for i in range(n):
    if (partner[i][0] in singal) and (partner[i][1] in singal):
        singal.remove(partner[i][0])
        singal.remove(partner[i][1])
if len(singal)==0:
    print(0,end="")
else:
    singal.sort()
    print(len(singal))
    print(' '.join(singal))