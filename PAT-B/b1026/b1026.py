from math import ceil, floor

def round_common(frac, preci = 0):
	return round(frac + 10e-9, preci)

def calc(second):
	hour = floor(second / (60*60))
	minute = floor((second - hour*60*60) / 60)
	second = int(round_common(second - hour*60*60 - minute*60))
	return ('{:02d}:{:02d}:{:02d}'.format(hour, minute, second))

def main():
	start, end = list(map(int, '3600 5343'.split()))
	length = (end - start) / 100
	print(calc(length))

if __name__ == '__main__':
	main()