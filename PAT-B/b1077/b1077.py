
def calc(ins):
	score = list(map(int, ins.split(' ')))
	group = []
	for i, s in enumerate(score[1:]):
		if s >= 0 and s <= m:
			group.append(s)
	group.remove(max(group))
	group.remove(min(group))
	average = float(sum(group)) / len(group)

	result = (score[0] + average) / 2
	result = round(result + 10e-10)

	return result


def main():
	inputs = str('1 50').split(' ')
	# inputs = str(input()).split(' ')
	global n
	global m
	n = int(inputs[0])
	m = int(inputs[1])
	for i in range(0, n):
		# score_list = str(input())
		score_list = str('30 250 -25 27 45 31')
		res = calc(score_list)
		print(res)


if __name__ == '__main__':
	main()