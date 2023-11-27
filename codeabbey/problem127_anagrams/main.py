def solve(d, w):
	sorted_word = ''.join(sorted(w))
	if not d.get(sorted_word):
		return 1
	else:
		return d[sorted_word]-1

def load_dictionary():
	print('loading dictionary of words...')
	f = open('words.txt', mode='r')
	d = {}
	word = f.readline()
	while word != '':
		sorted_word = ''.join(sorted(word.strip()))
		if not d.get(sorted_word):
			d[sorted_word] = 1
		else:
			d[sorted_word] += 1
		word = f.readline()
	f.close()
	print('done')
	return d

if __name__ == '__main__':
	d = load_dictionary()
	#print(d)
	n = int(input().strip())
	for i in range(n):
		w = input().strip()
		print(solve(d, w), end=' ')
	print()
