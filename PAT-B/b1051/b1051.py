import math

def pole2dec(r, p):
	a = r * math.cos(p)
	b = r * math.sin(p)
	return [a,b]

def multi(a, b):
	return [a[0]*b[0] - a[1]*b[1], a[1]*b[0] + a[0]*b[1]]

if __name__ == '__main__':
	r1, p1, r2, p2 = list(map(float, input().split()))
	# dig1 = pole2dec(2.3, 3.5)
	# dig2 = pole2dec(5.2, 0.4)
	dig_a, dig_b = multi(pole2dec(r1,p1), pole2dec(r2,p2))
	print('{:.2f}{:+.2f}i'.format(dig_a, dig_b))
