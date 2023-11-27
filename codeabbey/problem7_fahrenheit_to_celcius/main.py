import math

def rounding(n):
	neg = False
	if n < 0:
		neg = True
		n = n * -1
	if n % 1 >= 0.5:
		n = math.floor(n) 
		n = n + 1
	else:
		n = math.floor(n)
	
	if neg:
		n = n * -1
	
	return n

def solve(data):
	return [rounding((d - 32)*(5/9)) for d in data]

if __name__ == '__main__':
	data = list(map(lambda n: int(n.strip()), input().strip().split(' ')))
	print(*solve(data[1:]))
