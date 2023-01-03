def main():
	x, y = list(map(int, input().split()))
	multi = x * y
	multi = int(str(multi)[::-1])
	print(multi)


if __name__ == '__main__':
	main()