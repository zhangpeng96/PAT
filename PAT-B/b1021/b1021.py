from collections import Counter

def main():
	ins = list(str('100311'))
	result = sorted(Counter(ins).items(), key = lambda d: d[0])
	for res in result:
		# print(res[0] + ':' + res[1])
		print('%s:%s' % (res[0], res[1]))

if __name__ == '__main__':
	main()