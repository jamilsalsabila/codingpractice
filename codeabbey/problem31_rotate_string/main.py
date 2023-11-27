def solve(d, s):
	if d == len(s):
		return s
	elif d < 0:
		tmp = [' ' for _ in range(d*-1)]
		ls = list(s)
		tmp_i = 0
		for i in range(len(ls)-d*-1, len(ls)):
			tmp[tmp_i] = ls[i]
			tmp_i = tmp_i + 1
		for i in range(len(s)-d*-1-1, -1, -1):
			ls[i+d*-1] = ls[i]
		tmp_i = 0
		for i in range(0, d*-1):
			ls[i] = tmp[tmp_i]
			tmp_i = tmp_i + 1
		return ''.join(ls)
	elif d > 0:
		tmp = [' ' for _ in range(d)]
		ls = list(s)
		tmp_i = 0
		for i in range(0, d):
			tmp[tmp_i] = ls[i]
			tmp_i = tmp_i + 1
		for i in range(0+d, len(ls)):
			ls[i-d] = ls[i]
		tmp_i = 0
		for i in range(len(ls)-d, len(ls)):
			ls[i] = tmp[tmp_i]
			tmp_i = tmp_i + 1
		return ''.join(ls)
		
if __name__ == '__main__':
	n = int(input().strip())
	for i in range(n):
		[d, s] = input().strip().split()
		print(solve(int(d), s), end=' ')
