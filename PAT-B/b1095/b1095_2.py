from collections import Counter

def fn1(data, level):
	result = list(filter(lambda x: x[1][1] == level, data.items()))
	result = sorted(result, key = lambda x:(-x[1][0], x[0]))
	if len(result):
		for res in result:
			print(res[0], res[1][0])
	else:
		print('NA')


def fn2(data, room):
	result = list(map(lambda x:x[1][0], list(filter(lambda x: x[1][2] == room, data.items()))))
	if len(result):
		print(len(result), sum(result))
	else:
		print('NA')


def fn3(data, date):
	result = list(map( lambda x:x[1][2], list(filter(lambda x: x[1][3] == date, data.items()))))
	count = dict(Counter(result))
	count = sorted(count.items(), key = lambda x:(-x[1], x[0]))
	if len(result):
		for res in count:
			print(res[0], res[1])
	else:
		print('NA')


def main():
	data = {}
	# key: uid, value: score, level, room, date, sid
	ins_count, query_count = list(map(int, input().split()))

	for i in range(0, ins_count):
		rec = input().split()
		data[rec[0]] = [int(rec[1]), rec[0][0], rec[0][1:4], rec[0][4:10], rec[0][10:14]]

	for i in range(0, query_count):
		command = input().split()
		op, dig = int(command[0]), command[1]
		print('Case {}: {} {}'.format(i+1, op, dig))
		if op == 1:
			fn1(data, dig)
		elif op == 2:
			fn2(data, dig)
		elif op == 3:
			fn3(data, dig)
		else:
			pass
	# print(data)



if __name__ == '__main__':
	main()