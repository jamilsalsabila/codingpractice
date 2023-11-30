def id_mtrx(n):
    m = []
    _n = n
    if n < 0:
        n *= -1
    for i in range(1, n + 1):
        r = [0 for _ in range(0, i - 1)]
        r.append(1)
        r = r + [0 for _ in range(i, n)]
        m.append(r)
    if _n < 0:
        for i in range(len(m) // 2):
            m[i], m[n - i - 1] = m[n - i - 1], m[i]
    return m


print(*id_mtrx(4), sep='\n')
print(*id_mtrx(-4), sep='\n')
