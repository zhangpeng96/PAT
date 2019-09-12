import os

N = 20

def calc(dec, x1, x2, forward):
	dec = 10 if dec == 0 else dec
	if x1 + x2 + forward >= dec:
		return [1, x1 + x2 + forward - dec]
	else:
		return [0, x1 + x2 + forward]


def wrapper(string):
	arr = [0 for i in range(N)]
	length = len(string)
	for i in range(0, length):
		if string[i].isdigit():
			arr[i] = int(string[i])
	return arr


def main():
	table = wrapper(str('23456')[::-1])
	num1 = wrapper(str('00000')[::-1])
	num2 = wrapper(str('12347')[::-1])
	result = [0 for i in range(N)]

	for i in range(0, N-1):
		res = calc(table[i], num1[i], num2[i], result[i])
		result[i] = res[1]
		result[i+1] = res[0]
	
	result = result[::-1]
	s = int(''.join(map(str, result)))
	print(s)


if __name__ == '__main__':
	main()
