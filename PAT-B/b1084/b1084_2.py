from collections import Counter

def main():
	# ins_n = int(input())
	# rand_num = list(map(int, input().split()))
	ins_n = int('8')
	rand_num = list(map(int, '3 5 8 6 2 1 4 7'.split()))
	order_num = list(x for x in range(1, ins_n + 1))
	diff_num = list(map(lambda x,y: abs(x-y), rand_num, order_num))
	data = sorted(list(set(diff_num)), reverse = True)
	for d in data:
		print('%s %s' % (d, diff_num.count(d)))

	# diff_num = Counter(diff_num)
	# diff_num = sorted(diff_num.items(), key = lambda d: d[0], reverse = True)
	print(data)
	# print(rand_num, order_num, diff_num)


if __name__ == '__main__':
	main()