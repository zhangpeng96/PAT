def big_divide(dividend, divisor):
	if dividend == 0:
		return (0, divisor)
	divisor = int(divisor)
	quotient = ''
	mod = 0
	for i in dividend:
		dig = mod*10 + int(i)
		quot = dig // divisor
		mod = dig % divisor
		quotient += str(quot)
	return (int(quotient), mod)

def main():
	dividend, divisor = '0 7'.split()
	result = big_divide(dividend, int(divisor))
	print(result[0], result[1])

if __name__ == '__main__':
	main()
