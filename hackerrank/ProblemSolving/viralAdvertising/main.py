def viralAdvertising(n) -> int:
	p = 5
	a = 0
	total = 0
	for i in range(n):
		a = p//2
		total += a
		p = a * 3
	return total

print(viralAdvertising(3))
