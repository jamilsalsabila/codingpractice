def divisibleSumPairs(n, k, arr):
	result = 0
	for i in range(0, n-1):
		for j in range(i+1, n):
			if (arr[i] + arr[j]) % k == 0:
				result += 1
				#print(f"({arr[i]} + {arr[j]}) % {k} = {(arr[i] + arr[j]) % k}")

	return result

print(divisibleSumPairs(6, 3, [1,3,2,6,1,2]))

