def calc(item):
	option = item.split(' ')
	mapper = {
		'A': 1, 'B': 2, 'C': 3, 'D': 4
	}
	for i, op in enumerate(option):
		op = op.split('-')
		if op[1] == 'T':
			return mapper[op[0]]


def main():	
	count = int(input())
	result = ''
	while count:
		item = str(input())
		result += str(calc(item))
		count = count - 1
	print(result)


if __name__ == '__main__':
	main()