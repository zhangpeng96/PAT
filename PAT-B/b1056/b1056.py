def main():
	number_list = '3 2 8 5'.split()
	combine_value = 0
	lst = []
	number_len = len(number_list)
	
	for i in range(0, number_len):
		for j in range(0, number_len):
			if i == j:
				continue
			combine = number_list[i] + number_list[j]
			combine_value += int(combine)
			lst.append(combine)

	lst.sort()
	print(lst)

	print(combine)

if __name__ == '__main__':
	main()