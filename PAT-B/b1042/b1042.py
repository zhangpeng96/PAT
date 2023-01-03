from collections import Counter

def main():
	ins = 'This is a simple TEST.  There ARE numbers and other symbols 1&2&3...........'
	lst = ''.join(filter(lambda y: y >= 'a' and y <= 'z', map(lambda x: x.lower(), ins)))
	result = dict(Counter(lst))
	result = sorted(result.items(), key = lambda x:(-x[1],x[0]), reverse = False)
	print('{0[0]} {0[1]}'.format(result[0]))

if __name__ == '__main__':
	main()

	# result = Counter(lst).most_common(1)