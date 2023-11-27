def breakingRecords(scores):
	result = [0, 0]
	maxMinCount = [scores[0], scores[0]]
	for i in range(1, len(scores)):
		if scores[i] > maxMinCount[0]:
			result[0] += 1
			maxMinCount[0] = scores[i]
		elif scores[i] < maxMinCount[1]:
			result[1] += 1
			maxMinCount[1] = scores[i]

	return result

print(*breakingRecords([12,24,10,24]))

