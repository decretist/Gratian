#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
from __future__ import print_function
import re
import sys
def main():
    file = open('./edF.txt', 'r').read()
    # (?<=...) positive lookbehind assertion.
    inscriptions = re.findall('(?:\<T I\>|(?<=\<T I\>))(.*?)' # inscription starts with inscription tag.
        '(?:'                   # non-capturing group.
            '\<1 C\>|'          # inscription ends with major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<T [PT]\>'        # or inscription or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 1277 inscriptions, found ' + str(len(inscriptions)) + ' inscriptions', file=sys.stderr)
    for inscription in inscriptions:
        inscription = re.sub('\<S \d{1,4}\>\<L 1\>', '', inscription) # remove page and line number tags.
        inscription = re.sub('\<P 1\>|\<P 0\>', '', inscription)    # remove Palea tags.
        inscription = re.sub('\-.*?\+', '', inscription)
        # inscription = re.sub(re.compile('\-\[.*?\]\+', re.S), '', inscription)
        inscription = re.sub(re.compile('\-.*?\+', re.S), '', inscription)
        inscription = re.sub('\s+', ' ', inscription)
        inscription = re.sub('^\s+', '', inscription) # remove leading whitespace characters
        inscription = re.sub('\s+$', '', inscription) # remove trailing whitespace characters
        print(inscription)

if __name__ == '__main__':
    main()
