import re, collections

# Spell Check program using algorithm originally
# summarized by Dr. Peter Norvig.
#	src: http://norvig.com/spell-correct.html
#	additional src: http://goo.gl/uaJ6DQ (Google)
#
# The algorithm used has 3 parts:
#	-The probability of the typed word being correctly typed by the user
#	-The offset probability of the user typing word, x, but initially meant word, y
# 	-Iteration of all possible outputs, and choosing a word which has the best probability


# Returning the words in a list as lower case and defining a word as a list of alphabetic characters
# Works because the singular version of a word is more probably than the possessive notation (dog, dog's)
def words(text): 
	return re.findall('[a-z]+', text.lower()) 

#Returns a dictionary with keys->words and values->number of occurences
def train(words):
    occurences = collections.defaultdict(lambda: 1) #Sets default values in a dictionary, less iteration to check if element is a part of the dictionary
    for w in words:
        occurences[w] += 1 #Incrementing occurence of word
    return occurences

#Edits can be deletion (deletes), swapping adajent letters (transposes), alteration (replaces), or inserting a letter (inserts)
#Returns a set of of all words one edit away from correct word
def edits1(word):
	splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	deletes = [a + b[1:] for a, b in splits if b]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts = [a + c + b     for a, b in splits for c in alphabet]
	return set(deletes + transposes + replaces + inserts)

#Returns a set of words with the possible edits
def known_edits2(word):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in lWords)

#A known word is most likely to be a word that has a vowel mistyped rather than 2 consonants, probable correct first letter, edit distances of around 1 or 2
def known(words): 
	return set(w for w in words if w in lWords)

# Highest Level Method
# Returns the possible word
def correct(word):
	candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word] # gets a set of words with the shortest edit distance from the typed word.
	return max(candidates, key=lWords.get) # returning the element of the set with the highest probability of being the correct word

alphabet = 'abcdefghijklmnopqrstuvwxyz'
lWords = train(words(file('/usr/share/dict/words').read()))

def main():
	while True:
		word = raw_input('>')
		print correct(word.lower())


if __name__ == "__main__":
	main()