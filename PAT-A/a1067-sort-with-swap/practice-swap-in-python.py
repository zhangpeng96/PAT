# import time

arr = [9, 0, 1, 4, 5, 7, 8, 2, 3, 6]

# arr[0], arr[7] = arr[7], arr[0]
# print(arr)

# WRONG WAY
# arr[0], arr[ arr[0] ] = arr[ arr[0] ], arr[0]
# print(arr)
# supposed to: [6, 0, 1, 4, 5, 7, 8, 2, 3, 9]
# actually to: [6, 0, 1, 4, 5, 7, 9, 2, 3, 6]

# RIGHT WAY
pos = arr[0]
arr[0], arr[pos] = arr[pos], arr[0]
print(arr)
