def solve(n, ns1, ns2):
    return list(map(lambda n, m: n+m, ns1, ns2))

if __name__ == '__main__':
    n = int(input().strip())
    ns1 = []
    ns2 = []
    for i in range(n):
        [a, b] = list(map(lambda n: int(n.strip()),input().strip().split(' ')))
        ns1.append(a)
        ns2.append(b)
    print(*solve(n, ns1, ns2))
