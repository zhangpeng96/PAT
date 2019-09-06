from collections import Counter

def change_map(char):
	global letter_map, result
	if letter_map[char]:
		result += char
		letter_map[char] -= 1

def main():
	ins = 'PPPPPPPPP'
	lst = ''.join(filter(lambda x: x in 'PATest', ins))

	global result, letter_map
	result = ''
	letter_map = dict(Counter(lst))
	# max_letter = max(letter_map.values())
	max_letter = max(letter_map.values()) if len(letter_map) else 0

	for i in range(0, max_letter):
		for char in 'PATest':
			change_map(char)

	print(result)

if __name__ == '__main__':
	main()