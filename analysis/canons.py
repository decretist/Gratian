#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 12 March 2014
# 17 February 2015
#
from __future__ import print_function
import re
import sys
def main():
    file = open('./edF.txt', 'r').read()
    # (?<=...) positive lookbehind assertion
    canons = re.findall('(?:\<T T\>|(?<=\<T T\>))(.*?)' # canon starts with text tag
        '(?:'                   # (?:...) non-capturing group
            '\<1 [CD][CP]?\>|'  # canon ends with start of next case or distinction,
            '\<3 \d{1,2}\>|'    # or start of next question,
            '\<4 \d{1,3}\>|'    # or start of next canon,
            '\<T [IPT]\>|'      # or inscription or dpc or text tag,
            '$'                 # or end of file
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline
    # print('expected 4394 canons, found ' + str(len(canons)) + ' canons', file=sys.stderr)
    for canon in canons:
        canon = re.sub('\<S \d{1,4}\>\<L 1\>', '', canon) # remove page and line number tags
        canon = re.sub('\<P 1\>|\<P 0\>', '', canon) # remove Palea start and end tags
        canon = re.sub('\-.*?\+', '', canon)
        canon = re.sub(re.compile('\-\[.*?\]\+', re.S), '', canon)
        canon = re.sub('\s+', ' ', canon)
        canon = re.sub('^\s+', '', canon) # remove leading whitespace characters
        canon = re.sub('\s+$', '', canon) # remove trailing whitespace characters
        print(canon)

if __name__ == '__main__':
    main()
