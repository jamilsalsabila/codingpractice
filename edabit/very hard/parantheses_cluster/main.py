def split(txt):
    r = []
    t = 0
    s = ""
    for c in txt:
        if c == "(":
            t += 1
            s += c
        if c == ")" and t > 0:
            t -= 1
            s += c
            if t == 0:
                r.append(s)
                s = ""
    return r
