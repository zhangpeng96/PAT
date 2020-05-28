
# input_a = input()
# input_b = input()

input_a = '3 1 2.4 0 3.2 5 0.0'
input_b = '2 2 1.5 1 0.5'


a_count, b_count = int(input_a[0]), int(input_b[0])
poly_a_coe, poly_a_exp = tuple(map(float, input_a.split()[2::2])), tuple(map(int, input_a.split()[1::2]))
poly_b_coe, poly_b_exp = tuple(map(float, input_b.split()[2::2])), tuple(map(int, input_b.split()[1::2]))

poly = {}

for a in range(a_count):
    for b in range(b_count):
        coe, exp = poly_a_coe[a] * poly_b_coe[b], poly_a_exp[a] + poly_b_exp[b]
        if exp in poly.keys():
            poly[exp] += coe
        else:
            poly[exp] = coe

poly = sorted(filter(lambda x: x[1] != 0.0, poly.items()), key = lambda x: -x[0])

print(poly)

print(len(poly), ' '.join( map(lambda x: '{:d} {:.1f}'.format(*x), poly) ))

# from itertools import product

# co = product(poly_a_coe, poly_b_coe)
# ep = product(poly_a_exp, poly_b_exp)
# print(list(co), list(ep))

