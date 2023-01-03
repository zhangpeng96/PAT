'''
16'48"
'''

def main():
	cake, city = list(map(int, input().split()))
	data = {i:0 for i in range(0, cake)}
	
	for c in range(0, city):
		for i, amount in enumerate(map(int, input().split())):
			data[i] += amount

	data = sorted(data.items(), key = lambda x:(x[1], -x[0]), reverse = True)
	max_sale = data[0][1]
	max_cake = [data[0][0] + 1]

	for cake in data[1:]:
		if cake[1] == max_sale:
			max_cake.append(cake[0] + 1)

	print(max_sale)
	print(' '.join(map(str, max_cake)))


if __name__ == '__main__':
	main()