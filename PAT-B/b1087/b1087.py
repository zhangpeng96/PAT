import math

def main():
	ins = 2
	num_list = list(map(lambda x: math.floor(x/(2*x-1)), [i for i in range(0, ins+1)]))
	num_list[0] = 1
	print(num_list)


if __name__ == '__main__':
	main()