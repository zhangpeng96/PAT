from collections import Counter

def main():
	ins = 'MMDFllldfsi ()'
	ins = map(lambda x: x.lower(), ins)
	ins = ''.join(filter(lambda x: x >= 'a' and x <= 'z', ins))
	string = list(map(lambda x: ord(x)-96, ins))
	str_sum = bin(sum(list(map(lambda x: ord(x)-96, ins))))
	str_bin = str(str_sum).replace('0b', '')

	count = { **{'0': 0, '1': 0}, **dict(Counter(str_bin)) }

	print(count['0'], count['1'])


if __name__ == '__main__':
	main()