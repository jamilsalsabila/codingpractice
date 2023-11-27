def anagram(s):
	if len(s) % 2 != 0:
		return -1
	
	s1 = [0 for _ in range(26)]
	s2 = [0 for _ in range(26)]
	
	for c in s[:len(s)//2]:
		s1[ord(c)-97] += 1
	
	for c in s[len(s)//2:]:
		s2[ord(c)-97] += 1

	#print(s[:len(s)//2])
	#print(s1)
	#print(s[len(s)//2:])
	#print(s2)

	needed1 = 0
	for i in range(26):
		if s1[i] < s2[i]:
			needed1 += abs(s1[i]-s2[i])
	needed2 = 0
	for i in range(26):
		if s2[i] < s1[i]:
			needed2 += abs(s2[i]-s1[i])
	
	needed = min(needed1, needed2)
	return needed 

print(anagram("aaabbb"))
print(anagram("ab"))
print(anagram("abc"))
print(anagram("mnop"))
print(anagram("xyyx"))
print(anagram("xaxbbbxx"))
print(anagram("asdfjoieufoa"))
print(anagram("fdhlvosfpafhalll"))
print(anagram("mvdalvkiopaufl"))
