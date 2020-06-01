

ins1 = '2 1 2.4 0 3.2'
ins2 = '2 2 1.5 1 0.5'

ins1 = input()
ins2 = input()

poly_a = dict(zip( map(int, ins1.split()[1::2]), map(float, ins1.split()[2::2]) ))
poly_b = dict(zip( map(int, ins2.split()[1::2]), map(float, ins2.split()[2::2]) ))
poly = {}

for key in (poly_a.keys() | poly_b.keys()):
    poly[key] = poly_a.get(key, 0) + poly_b.get(key, 0)

res = sorted(poly.items(), key = lambda x: -x[0])

print(len(res), ' '.join(map(lambda x: '{} {}'.format(*x), res)))


# from collections import Counter
# a, b = Counter(poly_a), Counter(poly_b)

# print(a, b, a+b)
