def solve(a, x, y):
	a.append(*[x if x < y else y])

if __name__ == '__main__':
	n = int(input().strip())
	a = []
	for i in range(n):
		[x, y] = map(lambda n: int(n.strip()), input().strip().split(' '))
		solve(a, x, y)
	print(*a)
