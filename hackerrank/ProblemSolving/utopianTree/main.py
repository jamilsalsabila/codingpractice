def utopianTree(n):
	if n == 0:
		return 1
	elif n == 1:
		return 2
	elif n % 2 == 0:
		i = 0
		sum = 1
		while i < n:
			sum = sum * 2 + 1
			i += 2
		return sum
	else:
		i = 1
		sum = 2
		while i < n:
			sum = sum * 2 + 2
			i += 2
		return sum

print(utopianTree(4))
print(utopianTree(1))
print(utopianTree(0))
