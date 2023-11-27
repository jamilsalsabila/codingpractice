def maxMin(k, arr):
	if k > len(arr):
		return "Invalid K"
	unfairness = 999999999
	arr.sort()
	for i in range(0, len(arr)-k+1):
		min, max = arr[i], arr[i+k-1]
		if max-min < unfairness:
			unfairness = max-min
	return unfairness
	
print(maxMin(4, [1,2,3,4,10,20,30,40,100,200]))
