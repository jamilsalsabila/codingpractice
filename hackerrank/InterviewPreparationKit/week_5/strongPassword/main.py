def minimumNumber(n, password):
	bin = [0 for _ in range(4)]
	special_characters = "!@#$%^&*()-+"
	for c in password:
		if ord(c) >= 48 and ord(c) <= 57:
			bin[0] += 1
		elif ord(c) >= 97 and ord(c) <= 122:
			bin[1] += 1
		elif ord(c) >= 65 and ord(c) <= 90:
			bin[2] += 1
		else:
			if c in special_characters:
				bin[3] += 1
			else:
				return "character unknown"
	ad = 0
	for _ in range(4):
		if bin[_] == 0:
			ad += 1
	#print("ad: ", ad)

	if n < 4:
		return 6-n
	elif n >= 4 and n < 6:
		if ad > 6-n:
			return ad
		else: 
			return 6-n 
	else:
		return ad

print(minimumNumber(5, '2bbbb'))
print(minimumNumber(5, '#**#*'))
