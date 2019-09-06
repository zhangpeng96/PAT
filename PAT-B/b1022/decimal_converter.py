def deci2any(digit, deci):
	digit_map = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
	digit_list = []
	result = ''
	while True:
		mod = digit % deci
		quoti = digit // deci
		digit_list.append(mod)
		digit = quoti
		if not quoti:
			break
	for i in digit_list[::-1]:
		result += str(digit_map[i])
	return result

def any2deci(digit, deci):
	return int(str(digit), deci)

print(f(10, 16))
