n = int(input().strip())
for _ in range(n):
	[x1, y1, x2, y2] = map(lambda x: int(x), input().strip().split())
	a = (y2-y1)/(x2-x1)
	b = y1 - (a*x1)
	print(f"({a} {b}) ")

