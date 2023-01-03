def get_pa(number, digit):
	result = ''
	for i in str(number):
		if i == str(digit):
			result += i
	result = int(result) if result != '' else 0
	return result

def main():
	a, da, b, db = list(map(int, '3862767 6 13530293 3'.split()))
	print('%d' % (get_pa(a, da) + get_pa(b, db)))


if __name__ == '__main__':
	main()