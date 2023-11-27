def towerBreakers(n, m):
	if m == 1 or n % 2 == 0:
		return 2
	else:
		return 1
print(towerBreakers(2, 2))
print(towerBreakers(1, 4))
print(towerBreakers(3, 5))
