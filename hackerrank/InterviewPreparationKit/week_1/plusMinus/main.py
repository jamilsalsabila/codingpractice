def plusMinus(arr):
	p = 0
	m = 0
	z = 0
	for i in arr:
		if i > 0:
			p += 1
		elif i < 0:
			m += 1
		else:
			z += 1
	print('%.6f'% (p/len(arr)))
	print('%.6f'% (m/len(arr)))
	print('%.6f'% (z/len(arr)))

print(plusMinus([-4,3,-9,0,4,1]))
