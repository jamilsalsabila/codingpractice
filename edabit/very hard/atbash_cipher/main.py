def atbash(txt):
    # A B C D E F G H I J K L M
    # Z Y X W V U T S R Q P O N
    _ = "ABCDEFGHIJKLMZYXWVUTSRQPON"
    __ = "abcdefghijklmzyxwvutsrqpon"
    s = ""
    for c in txt:
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            i = ord(c) - ord("A")
            if i <= 12:
                s += _[i + 13]
            elif i > 12:
                i = 26 - (i - 12)
                s += _[i - 13]
        elif ord(c) >= ord("a") and ord(c) <= ord("z"):
            i = ord(c) - ord("a")
            if i <= 12:
                s += __[i + 13]
            elif i > 12:
                i = 26 - (i - 12)
                s += __[i - 13]
        else:
            s += c
    return s
