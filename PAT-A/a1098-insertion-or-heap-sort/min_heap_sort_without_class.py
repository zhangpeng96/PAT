
def adjust_down(arr, low, high):
    root, child = low, low*2
    while child <= high:
        if child+1 <= high and arr[child] > arr[child+1]:
            child += 1
        if arr[root] <= arr[child]:
            break
        else:
            arr[root], arr[child] = arr[child], arr[root]
        root = child
        child = root*2
    return arr

def build_min_heap(arr):
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
    # return arr[1:]


seq = [53, 17, 78, 9, 45, 65, 87, 32]
heap = build_min_heap(seq)
print(heap)
# print(heap_sort(heap))
for s in heap_sort(heap):
    print(s)
