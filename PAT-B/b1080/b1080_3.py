def calc(gp, gmid, gfinal):
	name = []
	for i in (gp + gmid + gfinal):
		name.append(i.split(' ')[0])
	name = list(set(name))
	data = list(map(lambda x: {'name': x, 'score': [-1,-1,-1,0]}, list(set(name))))
	
	for i, chunk in enumerate([gp, gmid, gfinal]):
		for ch in chunk:
			print(ch.split(' ')[0], i, int(ch.split(' ')[1]))

	print(data)


def main():
	# ins = input()
	ins = '6 6 7'
	divi = list(map(int, ins.split(' ')))

	# data = {
	# 	'pro'
	# }
	# for length in divi:
	# 	for i in range(0, length):
	gp = ['01234 880','a1903 199','ydjh2 200','wehu8 300','dx86w 220','missing 400']
	gmid = ['ydhfu77 99','wehu8 55','ydjh2 98','dx86w 88','a1903 86','01234 39']
	gfinal = ['ydhfu77 88','a1903 66','01234 58','wehu8 84','ydjh2 82','missing 99','dx86w 81']
	calc(gp, gmid, gfinal)
	# for i in range(0, divi[0]):
	# 	# gp.append(str(input()))
	# 	gp.append()

	# for i in range(0, divi[1]):
	# 	gmid.append()
	# 	# gmid.append(str(input()))

	# for i in range(0, divi[2]):
	# 	gfinal.append()
	# 	# gfinal.append(str(input()))


if __name__ == '__main__':
	main()