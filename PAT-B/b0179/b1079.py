def pali(ins):
	return ins[::-1]

def calc(ins):
	count = 0
	while int(ins) != int(pali(ins)):
		sum_int = int(ins) + int(pali(ins))
		print('%s + %s = %s' % (ins, pali(ins), sum_int))
		ins = str(sum_int)
		count += 1
		if count >= 10:
			print('Not found in 10 iterations.')
			break
	if count < 10:
		print('%s is a palindromic number.' % ins)



def main():
	# ins = str(input())
	ins = '97152'
	# ins = '196'
	calc(ins)


if __name__ == '__main__':
	main()