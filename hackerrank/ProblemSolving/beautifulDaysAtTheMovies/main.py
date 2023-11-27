def beautifulDays(i, j, k):
	total = 0
	for num in range(i, j+1, 1):
		if abs(num - int(str(num)[::-1])) % k == 0:
			total += 1
	return total

print(beautifulDays(20, 23, 6))
