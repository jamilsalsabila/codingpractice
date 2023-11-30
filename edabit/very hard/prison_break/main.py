def freed_prisoners(prison):
    r = 0
    if prison[0] == 0:
        return r
    else:
        r += 1
        s = 1
        for i in range(1, len(prison)):
            if s % 2 == 1:
                if prison[i] == 0:
                    prison[i] = 1
                else:
                    prison[i] = 0
            if prison[i] == 1:
                r += 1
                s += 1
        return r


print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))  # 4

print(freed_prisoners([1, 1, 1]))  # 1

print(freed_prisoners([0, 0, 0]))  # 0

print(freed_prisoners([0, 1, 1, 1]))  # 0

print(freed_prisoners([1, 0, 0, 0, 0, 0, 0]))  # 2

print(freed_prisoners([1, 1, 1, 0, 0, 0]))  # 2

print(freed_prisoners([1, 0, 1, 0, 1, 0]))  # 6
