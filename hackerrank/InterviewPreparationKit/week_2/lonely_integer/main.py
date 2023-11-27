def lonelyinteger(a):
	d = {}
	for i in a:
		if d.get(i) == None:
			d[i] = 1
			continue
		d[i] += 1
	result = 0
	for k, v in d.items():
		if v == 1:
			result = k
			break
	return result

print(lonelyinteger([1,2,3,3,2,1,4]))
