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
		
		if data.get(school, False):
			data[school][0] += level * score
			data[school][1] += 1
		else:
			data[school] = [0.0, 0]
	print(data)


if __name__ == '__main__':
	main()