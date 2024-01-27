def collect(s, n):
    from re import findall
    return sorted(findall('(\w{{{}}})'.format(n), s), key=lambda s: s[0])


print(collect("intercontinentalisationalism", 6))
print(collect("strengths", 3))
print(collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15))
