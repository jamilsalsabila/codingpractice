def pickingNumbers(a):
	a.sort()
	result = 0
	start = 0
	end = 0
	while end < len(a):
		n = a[end]
		end += 1
		while end < len(a) and abs(n - a[end]) <= 1:
			end += 1
		d = end - start
		if result < d:
			result = d
		start = end

	return result


print(pickingNumbers([1,1,2,2,4,4,5,5,5]))

