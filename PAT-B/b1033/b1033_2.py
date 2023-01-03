def get_keys(ins):
	key_map = []
	i = 0
	while i < len(ins):
		if ins[i] == '+':
			key_map.append(ins[i+1].upper())
			ins = ins[:i+1] + ins[i+2:]
		else:
			key_map.append(ins[i].lower())
		i += 1	
	return key_map


def main():
	blind_keys = '7+IE.+L'
	input_str = '7_This_is_a_test.'
	for key in get_keys(blind_keys):
		input_str = input_str.replace(key, '')
	print(input_str)


if __name__ == '__main__':
	main()