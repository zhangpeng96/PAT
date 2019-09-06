import math

def find_nearest(num):
	if num < 1:
		return 0
	elif num < 7:
		return 1
	else:
		return math.floor((num + 1) / 4)

def draw(n):
