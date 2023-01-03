def swap(lists):
	lists[0], lists[1] = lists[1], lists[0]
	return lists

def main():
	digit_count = swap(list(map(int, '2 2 0 0 0 3 0 0 1 0'.split())))
	digit_map = swap(list(range(0, 10)))
	digit_list = []
	for i, count in enumerate(digit_count):
		digit_list.extend(count * [digit_map[i]])
	number = ''.join(map(str, digit_list))
	print(number)

if __name__ == '__main__':
	main()