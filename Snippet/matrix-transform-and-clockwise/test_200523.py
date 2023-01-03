from dis import dis


def paint(matrix, m, n):
    for i in range(m):
        print(' '.join(
            map( lambda x: '{:> 3}'.format(x), matrix[i*n : (i+1) * n] )
        ))


data = [i for i in range(1, 13)]

paint(data, 3, 4)

# print(data[0::4], data[1::4])
# 
# print(data[0:4], data[4:8])
print(2,3, data[ (2-1)*4 + 3 -1 ])
# data[0::4] = [0,0,0]
def test1():
    data[0::4] = [0,0,0]
    # paint(data, 3, 4)

def test2():
    data[0] = 0
    data[5] = 0
    data[9] = 0

# dis(test1)
# print('*'*25)
# dis(test2)
# # test1()
# # 
# paint(data, 3, 4)
# 
# 
# 
# 