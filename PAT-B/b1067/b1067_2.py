def main():
	password, limit = input().split()
	limit = int(limit)
	count = 0
	pw_list = []
	
	ins = ''
	while ins != '#':
		ins = input()
		pw_list.append(ins)
	pw_list.pop()

	for pw in pw_list:
		count += 1
		if count > limit:
			print('Account locked')
			break
		if pw == password:
			print('Welcome in')
			break
		else:
			print('Wrong password: ' + pw)



if __name__ == '__main__':
	main()