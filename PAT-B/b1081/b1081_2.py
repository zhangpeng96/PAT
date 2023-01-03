def calc(ins):
	count = {
		'digit': 0,
		'alpha': 0,
		'speical': 0,
		'dot': 0
	}
	if len(ins) < 6:
		return 'Your password is tai duan le.'
	else:
		for char in ins:
			if char.isdigit():
				count['digit'] += 1
			elif char.isalpha():
				count['alpha'] += 1
			elif char == '.':
				count['dot'] += 1
			else:
				count['speical'] += 1
		
		if count['speical']:
			return 'Your password is tai luan le.'
		else:
			if count['digit'] == 0 and count['alpha']:
				return 'Your password needs shu zi'
			if count['digit'] and count['alpha'] == 0:
				return 'Your password needs zi mu.'
			if count['digit'] and count['alpha']:
				return 'Your password is wan mei.'


def main():
	# ins_list = ['123s','zheshi.wodepw','1234.5678','WanMei23333','pass*word.6']
	ins_list = []
	ins_count = int(input())
	for i in range(0, ins_count):
		ins_list.append(str(input()))
	
	for ins in ins_list:
		print(calc(ins))


if __name__ == '__main__':
	main()
