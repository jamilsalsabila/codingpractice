def countingValleys(steps, path):
	i = 0
	c = 0
	result = 0
	while i < steps:
		while i < steps and path[i] == 'D':
			i += 1
			c -= 1
		
		while i < steps and path[i] == 'U':
			i += 1
			c += 1

			if c == 0:
				result += 1
	
	return result

print(countingValleys(8, 'UDDDUDUU'))
print(countingValleys(8, 'DUUUDUDD'))

#     /\/\
# _  /    \_
#  \/
