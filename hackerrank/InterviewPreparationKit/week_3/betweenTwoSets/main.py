import math

def getTotalX(a, b):
	LCM_A = Lcm(a)
	GCD_B = Gcd(b)
	result = 0
	LCM_A_CPY = LCM_A
	while LCM_A <= GCD_B:
		if GCD_B % LCM_A == 0:
			result += 1
		LCM_A = LCM_A + LCM_A_CPY

	return result

def lcm(a, b):
	return a * (b // gcd(a,b))

def gcd(a, b):
	return math.gcd(a, b)

def Lcm(a):
	result = a[0]
	for i in range(1, len(a)):
		result = lcm(result, a[i])
	return result

def Gcd(b):
	result = b[0]
	for i in range(1, len(b)):
		result = gcd(result, b[i])
	return result

a = [2, 6]
b = [24, 36]
print(getTotalX(a, b))
