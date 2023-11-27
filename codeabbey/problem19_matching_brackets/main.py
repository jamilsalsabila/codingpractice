def solve(s, d):
	stck = []
	for c in s:
		if c == '(' or c == '[' or c == '{' or c == '<':
			stck.append(c)
		elif c == ')' or c == ']' or c == '}' or c == '>':
			if len(stck) == 0:
				return 0
			p = stck.pop()
			if p != d[c]:
				return 0
	if len(stck) != 0:
		return 0
	return 1

def input(d):
	n = int(input().strip())
	for _ in range(n):
		s = input()
		r = solve(s, d)
		print(r, end=' ')

def init():
	d = {']':'[', ')':'(', '}':'{', '>':'<'}
	return d

if __name__ == '__main__':
	d = init()
	input(d)
