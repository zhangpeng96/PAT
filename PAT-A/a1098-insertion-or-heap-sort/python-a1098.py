"""
    @name     : a1098
    @version  : 21.0201
    @author   : zhangpeng96
    @time     : 50'12"
    @accepted : all
"""

def insertion_feature(a, b):
    inserted = 1
    while b[inserted] >= b[inserted-1]:
        inserted += 1
        if inserted == len(b)-1:
            return sorted(b)
    if a[inserted:] == b[inserted:]:
        ptr = inserted+1
        return sorted(b[:ptr]) + b[ptr:]
    else:
        return []

def adjust_down(arr, low, high):
    root, child = low, low*2
    while child <= high:
        if child+1 <= high and arr[child] < arr[child+1]:
            child += 1
        if arr[root] >= arr[child]:
            break
        else:
            arr[root], arr[child] = arr[child], arr[root]
        root = child
        child = root*2
    return arr

def build_max_heap(arr):
    length = len(arr)
    arr = [0] + arr
    parent = length//2
    while parent:
        arr = adjust_down(arr, parent, length)
        parent -= 1
    return arr[1:]

def heap_sort(arr):
    i = len(arr)
    arr = [0] + arr
    while i > 1:
        arr[1], arr[i] = arr[i], arr[1]
        arr = adjust_down(arr, 1, i-1)
        i -= 1
        yield arr[1:]

# a = list(map(int, '3 1 2 8 7 5 9 4 6 0'.split()))
# b = list(map(int, '1 2 3 7 8 5 9 4 6 0'.split()))

# a = list(map(int, '3 1 2 8 7 5 9 4 6 0'.split()))
# b = list(map(int, '6 4 5 1 0 3 2 7 8 9'.split()))

count = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

next_step = insertion_feature(a, b)
if next_step:
    print('Insertion Sort')
    print(' '.join(map(str, next_step)))
else:
    print('Heap Sort')
    build_heap = build_max_heap(a)
    heap = heap_sort(build_heap)
    while next(heap) != b:
        pass
    print(' '.join(map(str, next(heap))))
