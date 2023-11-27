def caesarCipher(s, k):
	def f(c):
		d = ord(c)
		if d >= 65 and d <= 90: 
			return chr(((d-65+k)%26)+65)
		elif d >= 97 and d <= 122:
			return chr(((d-97+k)%26)+97)
		else:
			return chr(d)

	return ''.join(list(map(f, s))) 


print(caesarCipher("middle-Outz", 2))
