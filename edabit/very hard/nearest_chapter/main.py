def nearest_chapter(chapt, page):
    m = 2 ** 32
    c = ''
    pp = 0
    for ch, pa in chapt.items():
        d = page - pa
        if d < 0:
            d *= -1
        if d <= m and pp < pa:
            m = d
            c = ch
            pp = pa
    return c


print(nearest_chapter({
    "Chapter 1": 1,
    "Chapter 2": 15,
    "Chapter 3": 37
}, 10))

print(nearest_chapter({
    "New Beginnings": 1,
    "Strange Developments": 62,
    "The End?": 194,
    "The True Ending": 460
}, 200))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5
}, 3))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5,
    "Chapter 1c": 50,
    "Chapter 1d": 100
}, 75))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5,
    "Chapter 1c": 50,
    "Chapter 1d": 100,
    "Chapter 1e": 200
}, 150))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5,
    "Chapter 1c": 50,
    "Chapter 1d": 100,
    "Chapter 1e": 200
}, 74))

print(nearest_chapter({
    "Chapter 1a": 1,
    "Chapter 1b": 5,
    "Chapter 1c": 50,
    "Chapter 1d": 100,
    "Chapter 1e": 200,
    "Chapter 1f": 400
}, 300))
