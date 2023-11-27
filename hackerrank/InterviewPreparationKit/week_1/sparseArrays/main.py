import json

def matchingStrings(strings, queries):
	results = []
	trie = {}
	for s in strings:
		p = trie
		for i in range(len(s)):
			if p.get(s[i]) == None:
				p[s[i]] = {"EOS": False, "n":0}
			if i+1 == len(s):
				p[s[i]]["EOS"] = True
				p[s[i]]["n"] += 1
				break
			if p[s[i]].get("next") == None:
				p[s[i]]["next"] = {}
			
			p = p[s[i]]["next"]
	
	#print(json.dumps(trie, indent=4))
	
	for q in queries:
		p = trie
		exist = True
		for i in range(len(q)):
			if p.get(q[i]) == None:
				exist = False
				break
			if i+1 == len(q):
				break
			p = p[q[i]]["next"]

		if exist and p[q[-1]]["EOS"]:
			results.append(p[q[-1]]["n"])
		elif exist and not p[q[-1]]["EOS"]:
			results.append(0)
		elif not exist:
			results.append(0)
	
	trie.clear()
	return results


strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']
print(*matchingStrings(strings, queries), sep='\n')
print('-------')
strings = ['def','de','fgh']
queries = ['de','lmn','fgh']
print(*matchingStrings(strings, queries), sep='\n')
print('-------')
strings = ['abcde','sdaklfj','asdjf','na','basdn','sdaklfj','asdjf','na','asdjf','na','basdn','sdaklfj','asdjf']
queries = ['abcde','sdaklfj','asdjf','na','basdn']
print(*matchingStrings(strings, queries), sep='\n')
print('-------')
