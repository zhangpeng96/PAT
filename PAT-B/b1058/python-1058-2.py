import re
s = re.escape(") (")
a = [int(i) for i in input().split()]
b = []
error = [0]*a[1]
for i in range(a[1]):
    b.append(input())
for i in range(a[0]):
    d = input()
    c = re.split(s,d[1:len(d)-1])
    grade = 0
    for j in range(len(c)):
        g = int(b[j][0])
        if c[j]!=b[j][4:]:
            error[j]+=1
            g = 0
        grade+=g
    print(grade)
e = sorted(error,reverse = True)
if e[0]==0:
    print('Too simple',end = "")
else:
    print(e[0],end = "")
    for i in range(len(error)):
        if error[i]==e[0]:
            print(" "+str(i+1),end = "")