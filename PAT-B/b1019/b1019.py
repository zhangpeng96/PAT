def sort(num, reverse = False):
	num = '{:04d}'.format(num)
	data = ''.join(sorted(num))
	if reverse:
		return int(data[::-1])
	else:
		return int(data)


def main():
	num = int(0)
	if num == 6174 or num == 0:
		print('{:04d} - {:04d} = {:04d}'.format(sort(num, 1), sort(num), sort(num, 1) - sort(num)))
	while not(num == 6174 or num == 0):
		num_a = sort(num, 1)
		num_b = sort(num)
		num = num_a - num_b
		print('{:04d} - {:04d} = {:04d}'.format(num_a, num_b, num))


if __name__ == '__main__':
	main()