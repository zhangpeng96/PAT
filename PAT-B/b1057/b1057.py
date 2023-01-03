from collections import Counter

def main():
	ins = 'PAT (Basic)'
	ins = map(lambda x: x.lower(), ins)
	ins = ''.join(filter(lambda x: x >= 'a' and x <= 'z', ins))
	string = list(map(lambda x: ord(x)-96, ins))
	str_sum = bin(sum(list(map(lambda x: ord(x)-96, ins))))
	str_bin = str(str_sum).replace('0b', '')
	count = dict(Counter(str_bin))

	print(count['1'], count['0'])


if __name__ == '__main__':
	main()