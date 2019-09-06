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
	ins_count, query_count = list(map(int, '8 4'.split()))
	ins_list = ['B123180908127 99','B102180908003 86','A112180318002 98','T107150310127 62','A107180908108 100','T123180908010 78','B112160918035 88','A107180908021 98']
	for ins in ins_list:
		rec = ins.split()
		data[rec[0]] = [int(rec[1]), rec[0][0], rec[0][1:4], rec[0][4:10], rec[0][10:14]]

	# fn1(data, 'A')
	# fn2(data, '107')
	fn3(data, '180908')
	# print(data)



if __name__ == '__main__':
	main()