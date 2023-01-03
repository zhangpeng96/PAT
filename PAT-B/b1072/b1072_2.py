def main():
	people_count, item_count = list(map(int, input().split()))
	avoid_item = list(map(str, input().split()))

	people = count = 0
	for i in range(0, people_count):
		item = input()
		name = item.split()[0]
		item = item.split()[2:]
		found = list(filter(lambda x: x in avoid_item, item))
		if len(found):
			people += 1
			count += len(found)
			print('{}: {}'.format(name, ' '.join(found)))
	print(people, count)

if __name__ == '__main__':
	main()