def groupAnagrams(words):
	anagrams = {}
	
	for word in words:
		sortedWords = "".join(sorted(word))
		if sortedWords in anagrams:
			anagrams[sortedWords].append(word)
		else:
			anagrams[sortedWords] = [word]
			
	return list(anagrams.values())
