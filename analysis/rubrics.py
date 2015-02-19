#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 17 January 2015
#
from __future__ import print_function
import re
import sys
def main():
    file = open('./edF.txt', 'r').read()
    # (?<=...) positive lookbehind assertion
    rubrics = re.findall('(?:\<T R\>|(?<=\<T R\>))(.*?)' # rubric starts with rubric tag
        '(?:'                   # (?:...) non-capturing group
            '\<T [IPT]\>'       # rubric ends with inscription or dpc or text tag
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline
    # print('expected 3423 rubrics, found ' + str(len(rubrics)) + ' rubrics', file=sys.stderr)
    for rubric in rubrics:
        rubric = re.sub('\<P 1\>', '', rubric) # remove Palea start tag
        rubric = re.sub('\-.*?\+', '', rubric)
        rubric = re.sub(re.compile('\-\[.*?\]\+', re.S), '', rubric)
        rubric = re.sub('\s+', ' ', rubric)
        rubric = re.sub('^\s+', '', rubric) # remove leading whitespace characters
        rubric = re.sub('\s+$', '', rubric) # remove trailing whitespace characters
        print(rubric)

if __name__ == '__main__':
    main()
