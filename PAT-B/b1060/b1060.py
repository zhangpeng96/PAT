def main():
	# count = int(input())
	distance_list = list(map(int, '6 7 6 9 3 10 8 2 7 8'.split()))
	distance_set = list(set(distance_list))
	distance_set.sort(reverse = True)
	print(distance_set)

	for distance in distance_set:
		days = len(list(filter(lambda x: x>distance, distance_list)))
		print(days, distance)
		if days == distance:
			print(days)
			break

if __name__ == '__main__':
	main()