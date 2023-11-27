def saveThePrisoner(n, m, s) -> int:
	return (((m % n) - 1 + (s - 1)) % n) + 1

print(saveThePrisoner(4, 6, 2))
print(saveThePrisoner(5, 2, 1))
print(saveThePrisoner(5, 2, 2))
print(saveThePrisoner(7, 19, 2))
print(saveThePrisoner(3, 7, 3))

