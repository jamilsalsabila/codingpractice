def twoArrays(k, A, B):
	A.sort()
	B.sort()
	n = len(A)
	for i in range(n):
		if A[i] + B[n-1-i] < k:
			return 'NO'
	return 'YES'

print(twoArrays(10, [2, 1,3], [7, 8, 9]))
print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))
