def solve(primes, _):
	return primes[_]

def start(primes):
	n = int(input().strip())
	testcase = list(map(lambda n: int(n.strip()), input().strip().split()))
	for _ in range(n):
		print(solve(primes, testcase[_]-1), end=' ')

def init():
	start = 2
	end = 3000000
	idx = [0 for _ in range(0, end+1)]
	for i in range(start, end+1):
		if idx[i] != -1:
			idx[i] = 1
		else:
			continue
		j = i + i
		while j < end+1:
			if idx[j] != -1:
				idx[j] = -1
			j += i
	primes = []
	for i in range(start, end+1):
		if idx[i] == 1:
			primes.append(i)
	idx.clear()
	return primes
	
if __name__ == '__main__':
	primes = init()
	start(primes)
