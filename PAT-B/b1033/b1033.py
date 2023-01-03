def get_keys(ins):
	key_map = []
	for i, k in enumerate(ins):
		if k == '+':
			key_map.append(ins[i+1].upper())
		else:
			key_map.append(ins[i].lower())
	return key_map





def main():
	blind_keys = '7+IE.+L'
	print(get_keys(blind_keys))



if __name__ == '__main__':
	main()