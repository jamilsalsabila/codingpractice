def flippingMatrix(matrix):
	n = len(matrix[0]) // 2
	d = len(matrix[0])
	result = 0
	for i in range(n):
		for j in range(n):
			mx = max([matrix[i][j],matrix[i][d-1-j],matrix[d-1-i][j],matrix[d-1-i][d-1-j]])
			result += mx
	return result

matrix = [[112,  42,  83, 119],
			 [ 56, 125,  56,  49],
			 [ 15,  78, 101,  43],
			 [ 62,  98, 114, 108]
			]
print(flippingMatrix(matrix))
