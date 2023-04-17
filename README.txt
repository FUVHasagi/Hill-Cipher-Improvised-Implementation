THE (IMPROVISED) HILL CIPHER ENCODE, DECODE AND CRACKING MANIPULATION (BUT USABLE)

LITERATURE REVIEW:
- Hill cipher, invented by Lester S. Hill in 1929 based on the using of matrix multiplication between a secret matrix size nxn
 which will serve as a key and the text message be divided in to group of n characters which then will be translated to vector numbers
- Original Hill Cipher used 26 elementary characters then using the modulo calculation which will quite difficult (at least for me) when
 coding and it will become extremely more complicated for the computer when we expand it in to more characters (Vietnamese for example)
**********************
UPGRADES:
- Instead of translating the texts string to a texts string, I decided to translating a texts string to a numbers string that can take 
out the number and decoding later. This doesn't affect much on the overall guarantee after all since it still lie in whether they can find
the key (or part of the original of the message or not)
- 26 elementary characters is a little too small, and I'm too lazy to write my own translation text <-> number so I used the Unicode
instead for convenient and for richer quantity of characters, now we can even use Vietnamese for the program
- The module cracking was added partly for in case we forget the key matrix but we still remember the first part of the large message,
but mostly to prove that our code still have vital drawbacks in security when some long enough part of our code is known (nxn first characters 
in this case)
**********************
FEATURES:
- This program has 3 modes:
	+ In the encoding mode, the user input a text message to encode into a string of number and a key matrix which we also include a
	inversible checking to ensure that the key matrix can be inverse and decoding the message later on. The numbers srting then can 
	be send via other form of communication (manually). It would take some time for the eavedropper to find the key, or the first part
	of the message (in case they have known the encoding procedure)
	+ In the decoding most, the user input a encoded string of numbers by the program and the key matrix, I here provide two modes 
	for the encoding key matrix (haven't been inversed yet) or the decoding message (have been inversed) it will output the original
	message
	+ In the cracking mode, the user entering the encoded message and the first part of the original message, the program will out put
	the full version of the original message
**********************
DRAWBACKS:
- I don't know how to create an interface so you have to interact to through elementary Python interface and choosing the modes by inputing
the appropriate number when needed
- The program still lack some errors checking steps so for the best operation please obey the program instruction
- The program will crashed immediately when copying the decoding message with redundant characters (especially the ' ')
**********************
CODING STRUCTURES:
The code can be dividing into four main part:
	+ The encoding and subordinate precedure and function
	+ The decoding and subordinate precedure and function
	+ The cracking precedure, consists of a key cracking precedure and a normal decoding precedure
	+ The main stream for the program
