from spellcheck import *
import sys

def main():
	spellchk = SpellCheck('/usr/share/dict/words')
	spellchk.run(sys.argv[1]) 



if __name__ == "__main__":
	main()