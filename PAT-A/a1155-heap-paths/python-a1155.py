"""
    @name     : a1155
    @version  : 21.0214
    @author   : zhangpeng96
    @time     : 61'04"
    @accepted : all
"""

# arr = list(map(int, '98 72 86 60 65 12 23 50'.split()))

length = int(input())
arr = list(map(int, input().split()))
arr = [None] + arr
heap = {'min': True, 'max': True}
path = []

def dfs(root):
    left, right = root*2, root*2+1
    # if root > length: return
    path.append(arr[root])
    if left > length: print(*path) # 叶子节点
    if right <= length:
        if arr[right] > arr[root]: heap['max'] = False
        elif arr[right] < arr[root]: heap['min'] = False
        dfs(right)
    if left <= length:
        if arr[left] > arr[root]: heap['max'] = False
        elif arr[left] < arr[root]: heap['min'] = False
        dfs(left)
    path.pop()

dfs(1)

if heap['max'] and not heap['min']:
    print('Max Heap')
elif heap['min'] and not heap['max']:
    print('Min Heap')
else:
    print('Not Heap')
