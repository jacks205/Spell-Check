import re, random
class Misspell:
	#Give list of words to mispell
	def __init__(self, wordList):
		self.wList = wordList

	def genWord(self):
		return self.misspelled(self.wList[random.randint(0,len(self.wList)-1)])

# Mispelling a word based on these types of incorrections while typing
#	-deletion (deletes)
# 	-swapping adajent letters (transposes)
#	-alteration (replaces)
#	-inserting a letter (inserts)
	#Returns a word mispelled
	def misspelled(self, word):
		vowels = 'aeiouy'
		consonants = 'bcdfghjklmnpqrstvwxyz'
		if len(word) < 9:
			mistakes = 1
		elif len(word) < 12:
			mistakes = 2
		elif len(word) < 17:
			mistakes = 3
		else:
			mistakes = 4
		newWord = word[0]
		prev = word[0]
		for i in word[1:]:
			if mistakes != 0:
				rNum = random.randint(1,10)
			else:
				rNum = 5
			# if rNum == 1:
				#Do nothing...'Deletion'
			if rNum == 2:
				#Swapping adjacent letters
				newWord = newWord[:len(newWord)-2] + i + prev
			elif rNum == 3:
				#Alteration
				if i in vowels:
					c = vowels[random.randint(0, len(vowels)-1)]
					while i == c:
						c = vowels[random.randint(0, len(vowels)-1)]
				else:
					c = i
				newWord += c
			elif rNum == 4:
				newWord += i + i
			else:
				newWord += i
			prev = i
			mistakes -= 1
		if newWord == word:
			newWord += prev
		return newWord

# def words(text): 
# 	return re.findall('[a-z]+', text.lower()) 

# lWords = words(file('/usr/share/dict/words').read())

# miss = Misspelled(lWords)
# print miss.genWord()