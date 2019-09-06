import re

def select(sets, order):
	face_str = ''
	for i, face in enumerate(order):
		if face >= len(sets[i]) or face < 1:
			return r'Are you kidding me? @\/@'
		else:
			face_str += sets[i][face-1]
	face_str = face_str[:1] + '(' + face_str[1:]
	face_str = face_str[:-1] + ')' + face_str[-1:]
	return face_str


def main():
	sets_hand = re.findall(r'\[(.*?)\]', input())
	sets_eye = re.findall(r'\[(.*?)\]',input())
	sets_mouth = re.findall(r'\[(.*?)\]',input())
	count = int(input())
	orders = []
	for i in range(0, count):
		orders.append(
			list(map(int, input().split()))
		)
	# sets_hand = re.findall(r'\[(.*?)\]', r'[╮][╭][o][~\][/~]  [<][>]')
	# sets_eye = re.findall(r'\[(.*?)\]', r' [╯][╰][^][-][=][>][<][@][⊙]')
	# sets_mouth = re.findall(r'\[(.*?)\]', r'[Д][▽][_][ε][^]')
	sets = [sets_hand, sets_eye, sets_mouth, sets_eye, sets_hand]
	# order = [3,3,4,3,3]
	for order in orders:
		result = select(sets, order)
		print(result)

if __name__ == '__main__':
	main()
