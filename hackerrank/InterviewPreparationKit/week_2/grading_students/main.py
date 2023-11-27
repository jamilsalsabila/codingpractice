def validate(n):
	result = 0
	if 5 - (n % 5) < 3:
		result = n + (5 - (n % 5))
	else:
		result = n

	if result < 40:
		return n
	else:
		return result 

def gradingStudents(grades):
	return list(map(validate, grades))

print(*gradingStudents([84,29,57]), sep='\n')
