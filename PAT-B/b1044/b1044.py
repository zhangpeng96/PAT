
digit_map = ['tret', 'jan','feb','mar','apr','may','jun','jly','aug','sep','oct','nov','dec']
forward_map = ['tret', 'tam','hel','maa','huh','tou','kes','hei','elo','syy','lok','mer','jou']

def earth2mars(digit):
	global digit_map
	global forward_map
	digit_list = []
	deci = 13
	result = []
	while True:
		mod = digit % deci
		quoti = digit // deci
		digit_list.append(mod)
		digit = quoti
		if not quoti:
			break
	digit_list = digit_list[::-1]
	for i in digit_list[:-1]:
		result.append(forward_map[i])
	result.append(digit_map[digit_list[-1]])
	return ' '.join(result)

def mars2earth(mars_str):
	global digit_map
	global forward_map
	mars_list = mars_str.split()
	mars_number = ''
	digit_13 = ['0','1','2','3','4','5','6','7','8','9','A','B','C']

	if len(mars_list) > 1:
		mars_map = {**dict(zip(digit_map, digit_13)), **dict(zip(forward_map, digit_13))}
		for i in mars_list:
			mars_number += mars_map.get(i, '')
	elif len(mars_list) == 1:
		digit_forward = ['0','10','20','30','40','50','60','70','80','90','A0','B0','C0']
		mars_number = dict(zip(digit_map, digit_13)).get(mars_list[0], '')
		mars_number = dict(zip(forward_map, digit_forward)).get(mars_list[0], '')
	return int(str(mars_number), 13)

# print(earth2mars(1000))
# print(mars2earth('tam'))

def main():
	ins = []
	count = int(input())
	for i in range(0, count):
		ins.append(input())
	for i in ins:
		if i.isdigit():
			print(earth2mars(int(i)))
		else:
			print(mars2earth(i))

if __name__ == '__main__':
	main()