def migratoryBirds(arr):
	d = {i:0 for i in range(5)}
	for t in arr:
		d[t-1] += 1
	t = sorted(d.items(), key=lambda itms:(-itms[1],itms[0]))
	return t[0][0]+1

print(migratoryBirds([1,1,2,2,3,4,4,5]))
