def solve(data):
	min = 999999999
	max = -999999999
	for n in data:
		if n < min:
			min = n
		if n > max:
			max = n
	
	return [max, min]

if __name__ == '__main__':
	data = list(map(lambda n: int(n.strip()), input().strip().split(' '))) 
	
	print(*solve(data))
