#!/usr/bin/python
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
ignore = ['atque', 'quoque', 'neque', 'itaque', 'absque', 'apsque',
	  'abusque', 'adaeque', 'adusque', 'denique', 'deque',
	  'susque', 'oblique', 'peraeque', 'plenisque', 'quandoque',
	  'quisque', 'quaeque', 'cuiusque', 'cuique', 'quemque',
	  'quamque', 'quaque', 'quique', 'quorumque', 'quarumque',
	  'quibusque', 'quosque', 'quasque', 'quotusquisque',
	  'quousque', 'ubique', 'undique', 'usque', 'uterque',
	  'utique', 'utroque', 'utribique', 'torque', 'coque',
	  'concoque', 'contorque', 'detorque', 'decoque', 'excoque',
	  'extorque', 'obtorque', 'optorque', 'retorque', 'recoque',
	  'attorque', 'incoque', 'intorque', 'praetorque',
          'que']
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
