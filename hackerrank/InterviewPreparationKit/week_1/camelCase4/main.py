s = input().strip()
while s != '':
	result = ''
	if s[0] == 'S':
		ss = ''
		if s[2] == 'M':
			ss = s[4:-2]
		else:
			ss = s[4:]
		for c in ss:
			if ord(c) < 97:
				result += ' ' + c.lower()
			else:
				result += c	
		if s[2] == 'C':
			result = result.strip()
	elif s[0] == 'C':
		ss = s[4:].split(' ')
		if s[2] == 'C':
			result += ss[0].capitalize()
		else:
			result += ss[0]
		for i in range(1, len(ss)):
			result += ss[i].capitalize()
		if s[2] == 'M':
			result += '()'

	print(result)
	try:
		s = input().strip()
	except EOFError:
		break
