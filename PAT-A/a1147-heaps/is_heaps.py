def is_heap(arr):
    arr = [None] + arr
    min_heap, max_heap = True, True
    for child in range(2, len(arr)):
        parent = child//2
        if arr[parent] > arr[child]: min_heap = False
        if arr[parent] < arr[child]: max_heap = False
    if not min_heap and not max_heap:
        return False
    elif min_heap:
        return -1
    else:
        return 1
