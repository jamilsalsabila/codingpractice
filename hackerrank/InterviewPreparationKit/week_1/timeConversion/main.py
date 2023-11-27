def timeConversion(s):
	result = ''
	if s[-2:] == 'AM':
		if s[0:2] == '12':
			result += '00' + s[2:-2]
		else:
			result += s[0:-2]
	else:
		if s[0:2] == '12':
			result += s[0:-2]
		else:
			result += str(12 + int(s[0:2])) + s[2:-2]
	
	return result 

print(timeConversion('07:05:45PM'))
