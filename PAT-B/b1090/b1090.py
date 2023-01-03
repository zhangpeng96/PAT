def main():
	check, box = list(map(int, input().split()))
	check_list = []
	box_list = []
	for i in range(0, check):
		check_list.append(set(input().split()))
	for i in range(0, box):
		box_list.append(set( input().split()[1:] ))

	result = [True] * len(box_list)

	for i, box in enumerate(box_list):
		for check in check_list:
			# print(i, check, box)
			if check <= box:
				result[i] = False
				break

	for r in result:
		if r:
			print('Yes')
		else:
			print('No')


if __name__ == '__main__':
	main()