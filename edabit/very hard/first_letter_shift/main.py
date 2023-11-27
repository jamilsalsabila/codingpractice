def shift_sentence(txt):
    words = txt.split(" ")
    n = len(words)
    for i in range(n - 1):
        a = words[i][0]
        b = words[n - 1][0]
        words[i], words[n - 1] = b + words[i][1:], a + words[n - 1][1:]
    return " ".join(words)
