def separateNumbers(s):
	flag = False
	new_s = '' 
	for i in range(len(s)-1):
		new_s = s[:i+1]
		check_s = new_s 
		new_d = int(new_s)
		while len(check_s) < len(s):
			new_d = new_d + 1
			check_s += str(new_d)
		#print(check_s, s)
		#print(check_s == s)
		if check_s == s:
			flag = True
			break
	if flag:
		return f"YES {new_s}"
	return "NO"

print(separateNumbers('1234')) 
print(separateNumbers('91011')) 
print(separateNumbers('99100'))
print(separateNumbers('1346'))
print(separateNumbers('908988'))
