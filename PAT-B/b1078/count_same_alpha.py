def count_same_alpha(obj_list):
	count = 0
	start = obj_list[0]
	it = iter(obj_list)
	while next(it) == start:
		count += 1
	return count

def count_series_number(obj_list)

if __name__ == '__main__':
	arr = '111111453'
	result = count_same_alpha(arr)
	print(result)