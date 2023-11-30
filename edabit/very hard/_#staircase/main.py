def staircase(n):
    if n > 0:
        for i in range(n):
            print('_' * (n - i - 1) + '#' * (i + 1))
    elif n < 0:
        n = n * -1
        for i in range(n):
            print('_' * i + '#' * (n - i))
    else:
        print("")


# staircase(7)
staircase(-7)
