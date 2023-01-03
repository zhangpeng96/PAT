import math

def main():
	ins = int(input())
	value = lambda x: math.floor(x/2) +  math.floor(x/3) +  math.floor(x/5)
	num_list = list(map(value, [i for i in range(0, ins+1)]))
	print(len(set(num_list)))


if __name__ == '__main__':
	main()