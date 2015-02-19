#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    # (?<=...) positive lookbehind assertion.
    dicta = re.findall('(?:\<T [AP]\>|(?<=\<T [AP]\>))(.*?)'    # dictum starts with dictum ante or dictum post tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # dictum ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            '\<T [AIPRT]\>'      # or inscription or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 1277 dicta, found ' + str(len(dicta)) + ' dicta', file=sys.stderr)
    for dictum in dicta:
        dictum = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', dictum) # remove page and line number tags.
        dictum = re.sub('\<P 1\> \-\[PALEA\.\+', '', dictum)    # remove Palea tags.
        dictum = re.sub('\-.*?\+', '', dictum)
        dictum = re.sub(re.compile('\-\[.*?\]\+', re.S), '', dictum)
        dictum = re.sub('\s+', ' ', dictum)
        dictum = re.sub('^\s+', '', dictum) # remove leading whitespace characters
        dictum = re.sub('\s+$', '', dictum) # remove trailing whitespace characters

        print(dictum)

if __name__ == '__main__':
    main()
