def main():
	count = int(input())
	data = {}
	for i in range(0, count):
		key, value = list(map(int, input().split()))
		if not data.get(key):
			data[key] = value
		else:
			data[key] += value
	data = sorted(data.items(), key = lambda d: d[1], reverse = True)
	print(data[0][0], data[0][1])

if __name__ == '__main__':
	main()