def main():
	password, limit = r'Correct%pw 2'.split()
	limit = int(limit)
	count = 0
	pw_list = [r'correct%pw',r'Correct@PW',r'whatisthepassword!',r'Correct%pw']
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