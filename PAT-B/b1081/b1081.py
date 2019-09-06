def calc(ins):
	if len(ins) < 6:
		return 'Your password is tai duan le.'
	else:
		ins_tiny = ins.replace('.', '')
		for char in ins_tiny:
			digit_only = 1
			alpha_only = 1
			if char.isdigit() or char.isalpha():
				if char.isdigit():
					digit_only = 0
				if char.isalpha():
					alpha_only = 0
			else:
				return 'Your password is tai luan le.'
		print(alpha_only, digit_only)
		if alpha_only:
			return 'Your password needs zi mu.'
		if digit_only:
			return 'Your password needs shu zi'
		if alpha_only == 0 and digit_only == 0:
			return 'Your password is wan mei.'


def main():
	ins_list = ['123s','zheshi.wodepw','1234.5678','WanMei23333','pass*word.6']
	for ins in ins_list:
		print(calc(ins))



if __name__ == '__main__':
	main()
