
string = input()
length = len(string)
dp = [ [False] * (length+1) for _ in range(length+1) ]
ans = 1

for i in range(length):
    dp[i][i] = True
    if i < length-1 and string[i] == string[i+1]:
        dp[i][i+1] = True
        ans = 2

for L in range(3, length+1):
    for i in range(length+1-L):
        j = i + L -1
        if string[i] == string[j] and dp[i+1][j-1]:
            dp[i][j] = True
            ans = L

print(ans)
