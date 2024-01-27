def is_happy(n):
    while n != 4 and n != 1:
        m = 0
        while n != 0:
            m += (n % 10)**2
            n = n // 10
        n = m
    if n == 4:
        return False
    if n == 1:
        return True


a = [1, 10, 44, 67, 89, 139, 1327, 2871, 3970, 5209, 6329, 8888, 9331, 10000]
b = [True, True, True, False, False, True, False, False, True, False, True, False, True, True]

print(list(map(is_happy, a)) == b)