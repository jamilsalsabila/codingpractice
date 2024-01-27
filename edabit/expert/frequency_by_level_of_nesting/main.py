def freq_count(lst, el, lvl=0, d=None):
    if d is None:
        d = {}
    if not d.get(f"{lvl}"):
        d[f"{lvl}"] = 0
    for i in lst:
        if i == el:
            d[f"{lvl}"] += 1
        if type(i) is list:
            freq_count(i, el, lvl + 1, d)
    return [[int(k),v] for k, v in d.items()]


print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1))
print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5], 5], 5))
print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))
print("--------------")
print(freq_count([1, 1, 1, 1], 1))
print(freq_count([1, 1, 2, 2], 1))
print(freq_count([1, 1, 2, [1]], 1))
print(freq_count([1, 1, 2, [[1]]], 1))
print(freq_count([[[1]]], 1))
