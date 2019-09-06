import math

def isPrime(n):
	if not n % 2: return n == 2
	if not n % 3: return n == 3
	if not n % 5: return n == 5
	for p in range(7, int(math.sqrt(n))+1, 2):
		if not n % p: return False
	return True

def award_type(order):
	if order == 1:
		return 'Mystery Award'
	elif isPrime(order):
		return 'Minion'
	else:
		return 'Chocolate'


def main():
	check_dict = {}

	msg_count = int(input())
	for i in range(0, msg_count):
		check_dict[str(input())] = False

	query_count = int(input())
	for i in range(0, query_count):
		lst = str(input())
		if check_dict.get(lst, 'empty') == 'empty':
			print('%s: Are you kidding?' % lst)
		else:
			if check_dict[lst]:
				print('%s: Checked' % lst)
			else:
				print('%s: %s' % (lst, award_type(int(lst))))
			check_dict[lst] = True

if __name__ == '__main__':
	main()