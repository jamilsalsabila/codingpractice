def maximumPerimeterTriangle(sticks):
	sticks.sort()
	result = []
	for i in range(len(sticks)-2):
		substicks = sticks[i:i+3]
		if substicks[0] + substicks[1] > substicks[2]:
			result.append(substicks)
	if len(result) == 0:
		return [-1]
	else:
		result.sort(key=sum,reverse=True)
		return result[0]

print(maximumPerimeterTriangle([1,2,3,4,5,10]))
