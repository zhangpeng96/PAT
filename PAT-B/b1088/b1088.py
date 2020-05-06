def equation(x, y, p):
	# attempt to A
	if p[0] != None:
		a = p[0]
		b = int(str(int(a))[::-1])
		c = b / y
		if (abs(a - b) == x * c):
			return [a, b, c]
	# attempt to B
	if p[1] != None:
		b = p[1]
		c = b / y
		a = x * c + b
		if b == int(str(int(a))[::-1]):
			return [a, b, c]
	# attempt to C
	if p[2] != None:
		c = p[2]
		b = y * c
		a = x * c + b
		if b == int(str(int(a))[::-1]):
			return [a, b, c]
	return False

def main():
	# ins = int(48)
	# x, y = 3, 6
	ins, x, y = list(map(int, input().split()))
	solution = []
	result = []
	ins_list = [[ins, None, None], [None, ins, None], [None, None, ins]]

	for i, ins in enumerate(ins_list):
		rsl = equation(x, y, ins)
		if rsl:
			sense = ['']*3
			for j, se in enumerate(rsl):
				if se == rsl[i]:
					sense[j] = 'Ping'
				if se < rsl[i]:
					sense[j] = 'Gai'				
				if se > rsl[i]:
					sense[j] = 'Cong'
			solution.append(rsl + [' '.join(sense)])

	if len(solution) > 1:
		solution = sorted(solution, key = lambda x:x[0], reverse = True)
		print(solution[0][0], solution[0][3])
	elif len(solution) == 1:
		print(solution[0][0], solution[0][3])
	else:
		print('No Solution')




if __name__ == '__main__':
	main()