"""
    @name     : a1089
    @version  : 21.0130
    @author   : zhangpeng96
    @time     : 46'06"
    @accepted : all
    @desc     : p4要考虑插入排序的值有相同的情况 L12
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

def merge_sort(seq):
    k, n = 1, len(seq)
    while k < n:
        k, part = k*2, n//k
        for i in range(part):
            seq[ i*k : (i+1)*k ] = sorted(seq[ i*k : (i+1)*k ])
        seq[ part*k : n ] = sorted(seq[ part*k : n ])
        yield seq


# a = list(map(int, '3 1 2 8 7 5 9 4 6 0'.split()))
# b = list(map(int, '1 2 3 7 8 5 9 4 6 0'.split()))

# a = list(map(int, '3 1 2 8 7 5 9 4 0 6'.split()))
# b = list(map(int, '1 3 2 8 5 7 4 9 0 6'.split()))

count = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

next_step = insertion_feature(a, b)
if next_step:
    print('Insertion Sort')
    print(' '.join(map(str, next_step)))
else:
    print('Merge Sort')
    merge = merge_sort(a)
    while next(merge) != b:
        pass
    print(' '.join(map(str, next(merge))))

