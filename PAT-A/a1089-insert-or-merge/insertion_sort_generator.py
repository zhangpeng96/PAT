"""
    @name      : insertion sort with generator
    @desciption: 插入排序生成器
"""

def insertion_sort(arr):
    for index in range(1, len(arr)):
        temp = arr[index]
        pos = index

        while pos>0 and arr[pos-1] > temp:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = temp
        yield arr


if __name__ == '__main__':
    for i in insertion_sort([3, 1, 2, 8, 7, 5, 9, 4, 6, 0]):
        print(i)
