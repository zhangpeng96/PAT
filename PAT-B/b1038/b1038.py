'''
time-use: 6'41"
'''


from collections import Counter

def main():
	input_count = int(5)
	score_list = list(map(int, '60 75 90 55 75 99 82 90 75 50'.split()))
	query = list(map(int, '3 75 90 88'.split()))
	query_list = query[1:]
	score = dict(Counter(score_list))

	result = []

	for q in query_list:
		result.append(score.get(q, 0))
	
	print(' '.join(map(str, result)))

if __name__ == '__main__':
	main()