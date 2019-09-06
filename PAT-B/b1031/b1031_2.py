

def calc(id_num):
	number = 0
	calc_id = id_num[:-1]
	mod_map = ['1','0','X','9','8','7','6','5','4','3','2']
	weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
	for i, w in enumerate(weight):
		number += int(calc_id[i]) * w
	mods = number % 11
	return mod_map[mods]


if __name__ == '__main__':
	# count = int(input())
	# id_list = []
	# for i in range(0, count):
	# 	id_list.append(str(input()))
	id_list = ['37070419881216001X']
	all_pasted = 1
	for id_str in id_list:
		id_num = list(map(str, list(id_str)))
		if not (calc(id_num) == id_num[-1]):
			all_pasted = 0
			print(id_str)
	if all_pasted:
		print('All passed')