"""
    @name     : a1147
    @version  : 21.0214
    @author   : zhangpeng96
    @time     : 32'17"
    @accepted : all
"""

def is_heap(arr):
    min_heap, max_heap = True, True
    for child in range(2, len(arr)):
        parent = child//2
        if arr[parent] > arr[child]: min_heap = False
        if arr[parent] < arr[child]: max_heap = False
    if min_heap and not max_heap: print('Min Heap')
    elif max_heap and not min_heap: print('Max Heap')
    else: print('Not Heap')

def post_order(root, traversal):
    if root >= len(arr): return
    lchild, rchild = root*2, root*2+1
    post_order(lchild, traversal)
    post_order(rchild, traversal)
    traversal.append(arr[root])


count, length = map(int, input().split())
for _ in range(count):
    order = []
    arr = [None] + list(map(int, input().split()))
    is_heap(arr)
    post_order(1, order)
    print(*order)
