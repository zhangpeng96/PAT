def main():
	count = int(input())
	# float_list = list(map(float, '0.1 0.2 0.3 0.4'.split()))
	float_list = list(map(float, input().split()))
	
	length = len(float_list)
	all_data = []
	for i in range(0, length):
		for j in range(i, length):
			lst = []
			for k in range(i, j+1):
				lst.append(float_list[k])
			all_data.extend(lst)

	print('{:.2f}'.format(round(sum(all_data), 2)))

if __name__ == '__main__':
	main()

# float(decimal.Decimal(4.445).quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_HALF_UP))