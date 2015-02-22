#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 12 March 2014
#
from __future__ import print_function
import re
import sys
def main():
    file = open('./edF.txt', 'r').read()
    # (?<=...) positive lookbehind assertion
    themata = re.findall('(?:\<T Q\>|(?<=\<T Q\>))(.*?)' # thema starts with thema tag
        # (?:...) non-capturing group
        '(?:'                   
            '\<3 1\>'
        # re.S (re.DOTALL) makes '.' special character match any character including newline
        ')', file, re.S)        
    # print('expected 36 themata, found ' + str(len(themata)) + ' themata', file=sys.stderr)
    for thema in themata:
        thema = re.sub('\<S \d{1,4}\>\<L 1\>', '', thema) # remove page and line number tags
        thema = re.sub('\-.*?\+', '', thema) # remove comment
        thema = re.sub('\s+', ' ', thema)
        thema = re.sub('^\s+', '', thema) # remove leading whitespace characters
        thema = re.sub('\s+$', '', thema) # remove trailing whitespace characters
        print(thema)

if __name__ == '__main__':
    main()
