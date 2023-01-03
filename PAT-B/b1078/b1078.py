'''
https://pintia.cn/problem-sets/994805260223102976/problems/994805262018265088
'''

def compress(ins):
	ins += ' '
	result = ''
	compared = ins[0]
	count = 0
	for char in ins:
		if char == compared:
			count += 1
		else:
			counts = str(count) if count != 1 else ''
			result += counts + compared
			compared = char
			count = 1
	result = result.replace('1', '')
	return result


def decompress(ins):
	result = ''
	count_str = ''
	for char in ins:
		if char.isdigit():
			count_str += char
		else:
			count = int(count_str) if count_str != '' else 1
			while count:
				result += char
				count_str = ''
				count -= 1
	return result



def main():
	# action = input()
	# ins = str(input())
	# if action == 'D':
	# 	result = decompress(ins)
	# elif action == 'C':
	# 	result = compress(ins)
	# print(result)

	# ins = 'TTTTThhiiiis isssss a   tesssst CAaaa as'
	# print(compress(ins))
	ins = '5T2h4is i5s a3 te4st CA3a as10Zd2 '
	print(decompress(ins))


if __name__ == '__main__':
	main()