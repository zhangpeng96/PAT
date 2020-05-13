

weight = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
z_map = ['1','0','X','9','8','7','6','5','4','3','2']

def verify(id_str):
    checkout = False
    try:
        mod = sum(map(lambda x,w: int(x)*w,  id_str[:17], weight)) % 11
        checkout = True if id_str[-1] == z_map[mod] else False
    except:
        checkout = False
    return checkout


# count = int(input())
# number_list = [input() for _ in range(count)]
number_list = ['320124198808240056','12010X198901011234','110108196711301866','37070419881216001X']
# number_list = ['320124198808240056','110108196711301862']

wrong_list = list(filter(lambda x: not verify(x), number_list))

if wrong_list:
    print(len(wrong_list))
    [print(wrong) for wrong in wrong_list]
else:
    print('All passed')
