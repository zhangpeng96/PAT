from pprint import pprint
from dis import dis
from timeit import timeit

d = [i for i in range(1, 17)]
mx = [d[i*4 : (i+1)*4] for i in range(4)]

print(mx)


def paint(matrix):
    for row in matrix:
        print(' '.join(map(lambda x:'{: 3}'.format(x), row)))

# def turn(matrix):
#     if not matrix:
#         return []
#     res = []
#     top,left,bottom,right = 0,0,len(matrix)-1,len(matrix[0])-1
#     while top<=bottom and left<=right:
#         for col in range(left,right+1):
#             res.append(matrix[top][col])
            
#         for row in range(top+1,bottom+1):
#             res.append(matrix[row][right])
        
#         if top != bottom:
#             for col in range(right-1,left-1,-1):
#                 res.append(matrix[bottom][col])
        
#         if left != right:
#             for row in range(bottom-1,top,-1):
#                 res.append(matrix[row][left])
        
#         left +=1;top+=1;right-=1;bottom-=1;

#     return res

# print(turn(mx))



# def turn2(matrix):
#     if not matrix:
#         return []
#     clockwise = []
#     top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
#     rows, cols = bottom+1, right+1
#     print(top, left, bottom, right)
#     while top <= bottom and left <= right:
#         clockwise += [ matrix[top][col] for col in range(left, right+1) ]
#         clockwise += [ matrix[row][right] for row in range(top+1, bottom+1) ]
#         if top != bottom:
#             clockwise += [ matrix[bottom][col] for col in range(right-1, left-1, -1) ]
#         if left != right:
#             clockwise += [ matrix[row][left] for row in range(bottom-1, top, -1) ]
#         left, top, right, bottom = left+1, top+1, right-1, bottom-1
#     print(clockwise)
#     return [clockwise[r*cols : (r+1)*cols] for r in range(rows)]


# def turn2(matrix):
#     if not matrix:
#         return []
#     top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
#     rows, cols = bottom+1, right+1
#     res = [ [-1]*cols for _ in range(rows)]
#     print(res)
#     # print(top, left, bottom, right)
#     it = iter([i for i in range(1, 17)])
#     while top <= bottom and left <= right:
#         [ res[top].__setitem__(col, next(it)) for col in range(left, right+1) ]
#         [ res[row].__setitem__(right, next(it)) for row in range(top+1, bottom+1) ]
#         if top != bottom:
#             [ res[bottom].__setitem__(col, next(it)) for col in range(right-1, left-1, -1) ]
#         if left != right:
#             [ res[row].__setitem__(left, next(it)) for row in range(bottom-1, top, -1) ]
#         left, top, right, bottom = left+1, top+1, right-1, bottom-1
#     return res


def clockwise(elements, m, n):
    it = iter(elements)
    res = [ [None] * n for _ in range(m)]
    top, left, bottom, right = 0, 0, m - 1, n - 1
    while top <= bottom and left <= right:
        [ res[top].__setitem__(col, next(it)) for col in range(left, right+1) ]
        [ res[row].__setitem__(right, next(it)) for row in range(top+1, bottom+1) ]
        if top != bottom:
            [ res[bottom].__setitem__(col, next(it)) for col in range(right-1, left-1, -1) ]
        if left != right:
            [ res[row].__setitem__(left, next(it)) for row in range(bottom-1, top, -1) ]
        left, top, right, bottom = left+1, top+1, right-1, bottom-1
    return res

# series = [i for i in range(1, 55)]
# paint(clockwise(series, 9, 6))

series = [i for i in range(1, 82)]

def magic_test_1():
    # return [i for i in range(10)]
    [ series.__setitem__(i, 999) for i in range(81) ]

def magic_test_2():
#     data = []
#     for i in range(10):
#         data.append(i)
#     return data
    for i in range(81):
        series[i] = 99

# dis(magic_test_1)
# print(timeit(magic_test_2))
# series = [i for i in range(1, 82)]
# print(timeit(magic_test_1))
'''
6.869224
19.289859300000003

'''

def magic_fn_1():
    mx = [0, 0, 0, 0]
    mx[0], mx[1], mx[2], mx[3] = 999, 999, 999, 999

def magic_fn_2():
    mx = [0, 0, 0, 0]
    mx.__setitem__(0, 999)
    mx.__setitem__(1, 999)
    mx.__setitem__(2, 999)
    mx.__setitem__(3, 999)

def magic_fn_3():
    mx = [0, 0, 0, 0]
    # mx[0:4] = [999] * (3-0)
    mx[0:4] = [999,999,999,999]

print(timeit(magic_fn_1))
print(timeit(magic_fn_2))
print(timeit(magic_fn_3))

'''
101           0 LOAD_CONST               1 (<code object <listcomp> at, line 101>)
              2 LOAD_CONST               2 ('magic_test_1.<locals>.<listcomp>')
              4 MAKE_FUNCTION            0
              6 LOAD_GLOBAL              0 (range)
              8 LOAD_CONST               3 (16)
             10 CALL_FUNCTION            1
             12 GET_ITER
             14 CALL_FUNCTION            1
             16 POP_TOP
             18 LOAD_CONST               0 (None)
             20 RETURN_VALUE
************
104           0 SETUP_LOOP              24 (to 26)
              2 LOAD_GLOBAL              0 (range)
              4 LOAD_CONST               1 (16)
              6 CALL_FUNCTION            1
              8 GET_ITER
        >>   10 FOR_ITER                12 (to 24)
             12 STORE_FAST               0 (i)

105          14 LOAD_CONST               2 (99)
             16 LOAD_GLOBAL              1 (series)
             18 LOAD_FAST                0 (i)
             20 STORE_SUBSCR
             22 JUMP_ABSOLUTE           10
        >>   24 POP_BLOCK
        >>   26 LOAD_CONST               0 (None)
             28 RETURN_VALUE

'''