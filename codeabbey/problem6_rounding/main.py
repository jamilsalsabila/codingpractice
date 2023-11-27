import math

def solve(a, b):
	n = a / b
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
if __name__ == '__main__':
	n = int(input().strip())
	for _ in range(n):
		[a, b] = map(lambda n: int(n.strip()), input().strip().split(' '))
		print(solve(a, b), end=' ')
