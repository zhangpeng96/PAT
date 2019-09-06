import timeit

import math

# 性能最好的素数判断函数
def isPrime(n):
	if not n % 2: return n == 2
	if not n % 3: return n == 3
	if not n % 5: return n == 5
	for p in range(7, int(math.sqrt(n))+1, 2):
		if not n % p: return False
	return True

def isPrime2(n):
	for p in range(2, int(math.sqrt(n))+1):
		if not n % p: return False
	return True

if __name__ == '__main__':
	ts_start =  timeit.default_timer()
	prime_list = []
	for i in range(0, 1000000):
		if isPrime(i):
			prime_list.append(i)
	print(prime_list)
	print('{:.3f}ms'.format((timeit.default_timer() - ts_start)*1000))