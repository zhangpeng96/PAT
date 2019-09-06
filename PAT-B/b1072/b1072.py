def main():
	avoid_item = [2333, 6666]
	item_list = ['U 4 9966 6666 8888 6666', 'JJ 3 0012 6666 2333']
	for item in item_list:
		name = item.split()[0]
		item = list(map(int, item.split()[2:]))
		found = list(filter(lambda x: x in avoid_item, item))
		if len(found):
			print('{}: {}'.format(name, ' '.join()))
		print(found)


if __name__ == '__main__':
	main()