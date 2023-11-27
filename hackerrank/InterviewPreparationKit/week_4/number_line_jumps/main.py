def kangaroo(x1, v1, x2, v2):
	if v2 - v1 == 0:
		return "NO"
	x = (x2-x1) / (v1-v2)
	y = v1 * x + x1
	print(x, y)
	if y > 0 and x > 0 and y % 1.0 == 0.0 and x % 1.0 == 0.0:
		return "YES"
	else:
		return "NO"

print(kangaroo(2, 1, 1, 2))
print(kangaroo(21, 6, 47, 3))
print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
