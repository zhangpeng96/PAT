"""
    @name      : merge sort with generator
    @desciption: 归并排序生成器
    @url       : https://stackoverflow.com/questions/62993954/
"""

def merge_sort(arr):
    def merge_sort_rec(start, end):
        if end - start > 1:
            middle = (start + end) // 2

            yield from merge_sort_rec(start, middle)
            yield from merge_sort_rec(middle, end)
            left = arr[start:middle]
            right  = arr[middle:end]

            a, b, c = 0, 0, start

            while a < len(left) and b < len(right):
                if left[a] < right[b]:
                    arr[c] = left[a]
                    a += 1
                else:
                    arr[c] = right[b]
                    b += 1
                c += 1

            while a < len(left):
                arr[c] = left[a]
                a, c = a + 1, c + 1

            while b < len(right):
                arr[c] = right[b]
                b, c = b + 1, c + 1

            yield arr

    yield from merge_sort_rec(0, len(arr))


if __name__ == '__main__':
    for i in merge_sort([6,3,8,7,4,1,2,9,5,0]):
        print(i)
