#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 22 April 2014
#
# Usage: xque.py < input/Gratian0.txt > output/Gratian0.txt
# Usage: xque.py < input/Gratian1.txt > output/Gratian1.txt
# Usage: xque.py < input/Gratian2.txt > output/Gratian2.txt
#
import re
import sys
# http://snowball.tartarus.org/otherapps/schinke/intro.html
ignore = ['absque', 'abusque', 'adaeque', 'adusque', 'apsque',
	  'atque', 'attorque', 'concoque', 'contorque', 'coque',
	  'cuique', 'cuiusque', 'decoque', 'denique', 'deque',
	  'detorque', 'excoque', 'extorque', 'incoque', 'intorque',
	  'itaque', 'neque', 'oblique', 'obtorque', 'optorque',
	  'peraeque', 'plenisque', 'praetorque', 'quaeque', 'quamque',
	  'quandoque', 'quaque', 'quarumque', 'quasque', 'quemque',
	  'quibusque', 'quique', 'quisque', 'quoque', 'quorumque',
	  'quosque', 'quotusquisque', 'quousque', 'recoque',
	  'retorque', 'susque', 'torque', 'ubique', 'undique',
	  'usque', 'uterque', 'utique', 'utribique', 'utroque']
def main():
    string = sys.stdin.read()
    words = re.split('\W', string)
    for word in words:
        match = re.match(r'(\w+)que(?:\b)', word)
        if match:
            if word.lower() in ignore:
                print(word)
            else:
                print(match.group(1) + ' ' + 'xque')
        else:
            if word:
                print(word)
            else:
                pass

if __name__ == '__main__':
    main()
