con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']
vow = ['a', 'e', 'i', 'o', 'u']

[n, x0] = map(lambda n: int(n.strip()), input().strip().split())
ts = map(lambda n: int(n.strip()), input().strip().split())
for t in ts:
	result = ''
	#x = x0
	for _ in range(1, t+1):
		x0 = (445 * x0 + 700001) % 2097152
		if _ % 2 == 0:
			result += vow[x0 % 5]
		else:
			result += con[x0 % 19]
	
	print(result, end=' ')
print()
