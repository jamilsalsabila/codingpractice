def swap(c):
	if c == '0':
		return '1'
	return '0'

def flippingBits(n):
	return int(''.join(map(swap,'{:032b}'.format(n))),2)

print(flippingBits(9))
print(flippingBits(3))
print(flippingBits(2147483647))
print(flippingBits(1))
print(flippingBits(0))
