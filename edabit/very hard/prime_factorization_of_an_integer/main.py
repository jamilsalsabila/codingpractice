import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(num, p=None):
    if p is None:
        p = []
    if is_prime(num):
        p.append(num)
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if is_prime(i) and num % i == 0:
                p.append(i)
                prime_factors(num//i, p)
                break
    return p


print(prime_factors(47))
print(prime_factors(20))
print(prime_factors(100))
print(prime_factors(8912234))
