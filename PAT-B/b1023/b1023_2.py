def main():
	digit_count = list(map(int, '6 0 0 0 0 3 0 0 1 0'.split()))
	digit_map = list(range(0, 10))
	digit_list = []

	for i, count in enumerate(digit_count):
		digit_list.extend(count * [digit_map[i]])

	# print(digit_list)

	for i, dig in enumerate(digit_list):
		if dig != 0:
			digit_list[0], digit_list[i] = digit_list[i], digit_list[0] 
			break

	number = ''.join(map(str, digit_list))
	print(number)

if __name__ == '__main__':
	main()