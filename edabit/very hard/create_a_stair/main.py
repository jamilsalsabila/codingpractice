def stair(steps):
    if steps == 0:
        return '___'
    s = ' '*(2*steps)+'_\n'
    steps -= 1
    while steps != 0:
        s += ' '*(2*steps)+'_|\n'
        steps -= 1
    s += '_|'
    return s


print(stair(1))
print(stair(2))
print(stair(3))
print(stair(4))
