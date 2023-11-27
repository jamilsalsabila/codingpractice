from functools import reduce

# cara lain
#def count_bits(x):
#    c = 0
#    for i in range(32):
#        c += (x & 1)
#        x >>= 1
#    return c
			
if __name__ == '__main__':
	n = int(input().strip())
	nums = map(lambda n: int(n.strip()), input().strip().split())
	for num in nums:
		if num < 0:
			s = bin((1<<32)-(num*-1))[2:]
			print(reduce(lambda a,b: int(a) + int(b), s), end=' ')
		else:
			s = bin(num)[2:]
			print(reduce(lambda a,b: int(a) + int(b), s), end=' ')
	print()
