import os

N = 20


def calc(dec, x1, x2, step):
	dec = int(dec)
	x1 = int(x1)
	x2 = int(x2)
	# print(dec, x1, x2)
	dec = 10 if dec == 0 else dec
	if x1 + x2 + step >= dec:
		return [1, x1 + x2 + step - dec]
	else:
		return [0, x1 + x2 + step]

def wrapper(arr):
	length = len(arr)
	for i in range(length, N-1):
		arr += '0'
	return arr

def main():	
	table = wrapper(str(input())[::-1])
	num1 = wrapper(str(input())[::-1])
	num2 = wrapper(str(input())[::-1])

	result = [0 for i in range(N)]

	for i, dig in enumerate(table):
		if dig.isdigit():
			res = calc(dig, num1[i], num2[i], result[i])
		elif dig == 'd':
			res = calc(0, num1[i], num2[i], result[i])
		print(res)
		result[i] += res[1]
		result[i+1] += res[0]

	result = result[::-1]
	print(result)

if __name__ == '__main__':
	main()
