def main():
	data = {}
	count = int(input())

	for i in range(0, count):
		record = list(map(int, input().split()))
		data[record[1]] = '{} {}'.format(record[0], record[2])

	count = int(input())
	query = list(map(int, input().split()))

	for q in query:
		print(data[q])

if __name__ == '__main__':
	main()