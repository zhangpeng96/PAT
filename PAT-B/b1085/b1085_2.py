def main():
	count = int(5)
	data = {}
	level_map = {'B': 1/1.5, 'A': 1, 'T': 1.5}
	ins_list = ['A57908 85 Au','B57908 54 LanX','A37487 60 au','T28374 67 CMU','T32486 24 hypu','A66734 92 cmu','B76378 71 AU','A47780 45 lanx','A72809 100 pku','A03274 45 hypu']
	
	for ins in ins_list:
		uid, score, school = ins.split()
		level = level_map.get(uid[0])
		score = int(score)
		school = school.lower()

		if not data.get(school, False):
			data[school] = [0.0, 0]

		data[school][0] += level * score
		data[school][1] += 1

	data = dict([ (k, [int(v[0]), v[1]]) for k,v in data.items()])
	data = sorted(data.items(), key = lambda x:(-x[1][0], x[1][1],x[0]))

	print(len(data))

	prev_index = prev_score = -1

	for i, d in enumerate(data):
		if d[1][0] != prev_score:
			prev_index = i
		print(prev_index+1, d[0], d[1][0], d[1][1])
		prev_score = d[1][0]


if __name__ == '__main__':
	main()