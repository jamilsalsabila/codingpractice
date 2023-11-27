def same_vowel_group(words):
    s = set([])
    t = set([])
    r = []
    for c in words[0]:
        if c in "aiueo":
            s.add(c)
    for word in words[1:]:
        for c in word:
            if c in "aiueo":
                t.add(c)
        if t == s:
            r.append(word)
        t.clear()
    s.clear()
    return r
