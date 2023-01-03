import math

def calc(ins):
	name = str(ins.split(' ')[0])
	dot_x = int(ins.split(' ')[1])
	dot_y = int(ins.split(' ')[2])
	distance = math.sqrt(dot_x**2 + dot_y**2)
	return {'name': name, 'distance':distance}

def main():
	data = []
	ins_list = []
	ins_count = int(input())
	for i in range(0, ins_count):
		ins_list.append(str(input()))
	# ins_list = ['0001 5 7','1020 -1 3','0233 0 -1']
	for ins in ins_list:
		data.append(calc(ins))
	data = sorted(data, key = lambda e: e.__getitem__('distance'))
	# print(data)
	print('%s %s' % (data[0]['name'], data[-1]['name']))


if __name__ == '__main__':
	main()

