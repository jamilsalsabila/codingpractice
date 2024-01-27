import math


def simplify(txt):
    a, b = [int(c) for c in txt.split('/')]
    c = math.gcd(a, b)
    if c == b:
        return f"{int(a / c)}"
    n = int(a / c)
    d = int(b / c)
    return f"{n}/{d}"


print(simplify("4/6"))
print(simplify("10/11"))
print(simplify("100/400"))
print(simplify("1/3"))
print(simplify("4/2"))
