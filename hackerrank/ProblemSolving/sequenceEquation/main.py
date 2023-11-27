def permutationEquation(p):
	di = dict()
	ai = []
	for i in range(len(p)):
		di[p[i]] = i+1
	for i in range(len(p)):
		ai.append(di[di[i+1]])
	
	return ai

print(permutationEquation([2,3,1]))
print(permutationEquation([4,3,5,1,2]))
