xque.py
-------
Read detagged Latin text from standard input into a string.  Split
the string into a list on word boundaries.  Iterate over the string,
matching on words ending with "que".  Print the word if the word
does not end with "que", or if the word ends with "que", but the
ending is part of the word.  Print the word plus "xque" if the word
ends with "que", and the ending is used as an enclitic.
