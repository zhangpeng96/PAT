C,D,Dvg,N=map(int,input().split())
L=[list(map(float,input().split())) for _ in range(N)]
L.append([0,D])
L.sort(key=lambda x:x[1])
filter(lambda x:x[1]>D,L)
def tryDrive(s,gas,res):
    if s==len(L)-1:
        print('{:.2f}'.format(res))
        return
    right=min(D,L[s][1]+C*Dvg)
    r=max(i if L[i][1]<=right else s for i in range(s+1,len(L)))
    best=s
    for i in range(s+1,r+1):
        if L[i][0]<=L[s][0]:
            best=i
            break
    if r==s:
        d=L[s][1]+C*Dvg
        print('The maximum travel distance = {:.2f}'.format(d))
    elif best==s:
        tmp,sec=min((L[i][0],i) for i in range(s+1,r+1))
        cost=(L[sec][1]-L[s][1])/Dvg
        res+=(C-gas)*L[s][0]
        gas=C-cost
        return tryDrive(sec,gas,res)
    else:
        cost=(L[best][1]-L[s][1])/Dvg
        res+=(cost-gas)*L[s][0]
        gas=0
        return tryDrive(best,gas,res)

if L[0][1] == 0.0:
    res=tryDrive(0,0,0)
else:
    print('The maximum travel distance = 0.00')