"""
    @name     : a1101
    @version  : 21.0214
    @author   : zhangpeng96
    @time     : 15'00"
    @accepted : all
    @desc     : https://blog.csdn.net/qq_40728667/article/details/108003597
""" 

count = int(input())
array = list(map(int, input().split()))

sort = sorted(array)
leftMax, pivot = 0, []

for i in range(count):
    if array[i] > leftMax:
        leftMax = array[i]
        if array[i] == sort[i]:
            pivot.append(array[i])

pivot.sort()
print(len(pivot))
print(*pivot)
