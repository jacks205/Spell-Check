Spell-Check
===========

Spell Checker in Python

Use
----
Cloning and Running Program
<pre><code>git clone https://github.com/jacks205/Spell-Check.git
cd Spell-Check
make 0 or make 1</code></pre>

Removing .pyc files if needed
<pre><code>make realclean</code></pre>

Note: When using word generated mistakes, reoccuring words or letters may appear. Cause being that random numbers aren't always completely random when generated reoccuringly.

Algorithm
---------
Spell Check program using algorithm originally
summarized by Dr. Peter Norvig.
	src: <a href="http://norvig.com/spell-correct.html">How to Write a Spelling Corrector</a>
	additional src: <a href="http://goo.gl/uaJ6DQ">Google Algorithm Paper</a>

The algorithm used has 3 parts:
+ The probability of the typed word being correctly typed by the user
+ The offset probability of the user typing word, x, but initially meant word, y
+ Iteration of all possible outputs, and choosing a word which has the best probability

My altered algorithm used is faster than <code>O(n)</code> because I shortened the list of possible words based on the first letter. By creating a dictionary ordered by letter, the run time of the program would range closer to <code>O(1/26*n)</code>, where <code>n</code> is the number of words, and <code>1/26</code> stands for the alphabet. If n is a 


Main Challenge
--------------

Write a program that reads a large list of English words (e.g. from /usr/share/dict/words on a unix system) into memory, and then reads words from stdin, and prints either the best spelling suggestion, or "NO SUGGESTION" if no suggestion can be found. The program should print ">" as a prompt before reading each word, and should loop until killed.

Your solution should be faster than <code>O(n)</code> per word checked, where n is the length of the dictionary. That is to say, you can't scan the dictionary every time you want to spellcheck a word.

For example:

<pre><code>> sheeeeep

sheep

> peepple

people

> sheeple

NO SUGGESTION</code></pre>


The class of spelling mistakes to be corrected is as follows:

+ Case (upper/lower) errors: "inSIDE" => "inside"
+ Repeated letters: "jjoobbb" => "job"
+ Incorrect vowels: "weke" => "wake"
Any combination of the above types of error in a single word should be corrected (e.g. "CUNsperrICY" => "conspiracy").

If there are many possible corrections of an input word, your program can choose one in any way you like. It just has to be an English word that is a spelling correction of the input by the above rules.

Final step: Write a second program that *generates* words with spelling mistakes of the above form, starting with correctly spelled English words. Pipe its output into the first program and verify that there are no occurrences of "NO SUGGESTION" in the output.

Algorithm Source
----------------
Peter Norvig - <a href="http://norvig.com/spell-correct.html">How to Write a Spelling Corrector</a>
