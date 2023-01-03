def main():
	# count = int(input())
	distance_list = list(map(int, '6 7 6 9 3 10 8 2 7 8'.split()))
	distance_list.sort(reverse = True)
	distance_set = list(set(distance_list))
	distance_set.sort(reverse = True)
	print(distance_list)

	for i, distance in enumerate(distance_list):
		if distance == i:
			print(i, distance)

if __name__ == '__main__':
	main()