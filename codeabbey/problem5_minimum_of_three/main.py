if __name__ == '__main__':
	n = int(input().strip())
	for i in range(n):
		print(min(map(lambda n: int(n.strip()), input().strip().split(' '))), end=' ')
	
