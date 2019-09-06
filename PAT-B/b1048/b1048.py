def main():	
	num_a, num_b = list(map(lambda x: x[::-1], '1234567 368782971'.split()))
	len_sub = abs(len(num_a) - len(num_b))

	if len(num_a) < len(num_b):
		num_a += ''.join(map(str, [0]*len_sub))
	elif len(num_a) > len(num_b):
		num_b += ''.join(map(str, [0]*len_sub))

	result = []
	for i in range(0, len(num_a)):
		if (i+1) % 2:
			dig = str((int(num_a[i]) + int(num_b[i])) % 13)
			dig = dig.replace('10', 'J').replace('11', 'Q').replace('12', 'K')
		else:
			dig = int(num_b[i]) - int(num_a[i])
			dig = (10 + dig) if dig < 0 else dig
		result.append(str(dig))

	print(''.join(result[::-1]))


if __name__ == '__main__':
	main()