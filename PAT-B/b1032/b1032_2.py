'''
2019/08/31 20:29:42 部分正确
0 答案正确 28ms 3476 KB
1 答案正确 29ms 3412 KB
2 答案正确 28ms 3476 KB
3 运行超时 0 KB
'''

from collections import defaultdict
 
a, dd = int(input()), defaultdict(int)
for i in range(a):
    a, b = map(int, input().split())
    dd[a] += b
result = max(dd.items(), key=lambda c: c[1])
print(str(result[0]) + " " + str(result[1]))