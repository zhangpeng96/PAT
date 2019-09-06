def main():
	number_list = input().split()[1::]
	combine_value = 0
	number_len = len(number_list)
	
	for i in range(0, number_len):
		for j in range(0, number_len):
			if i == j:
				continue
			combine = number_list[i] + number_list[j]
			combine_value += int(combine)

	print(combine_value)

if __name__ == '__main__':
	main()