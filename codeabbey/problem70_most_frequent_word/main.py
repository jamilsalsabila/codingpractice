con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z']
vow = ['a', 'e', 'i', 'o', 'u']
words = {}
word_len = 6

mfw = ''
lmfw = 0

seed = int(input().strip())
for __ in range(900000):
	word = ''
	for _ in range(1, word_len+1):
		seed = (445 * seed + 700001) % 2097152
		if _ % 2 == 0:
			word += vow[seed % 5]
		else:
			word += con[seed % 19]
	if words.get(word) == None:
		words[word] = 1
	else:
		words[word] += 1
	
	if words[word] > lmfw:
		lmfw = words[word]
		mfw = word

print(mfw, lmfw)
