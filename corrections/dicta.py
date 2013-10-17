#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
# dicta.py | fmt > dicta.txt
#
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    toc = open('./toc.txt', 'r')
    dictionary = {}
    # (?<=...) positive lookbehind assertion.
    dicta = re.findall('(?:\<T [AP]\>|(?<=\<T [AP]\>))(.*?)'    # dictum starts with dictum ante or dictum post tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # dictum ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of Quaestio,
            '\<4 \d{1,3}\>|'    # or number of chapter,
            '\<P 1\>|'          # or Palea,
            '\<T [AIPT]\>'      # or inscriptio or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    print('expected 1277 dicta, found ' + str(len(dicta)) + ' dicta', file=sys.stderr)
    for dictum in dicta:
        dictum = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', dictum) # remove page and line number tags.
        dictum = re.sub('\<P 1\> \-\[PALEA\.\+', '', dictum)    # remove Palea tags.
        dictum = re.sub(re.compile('\-\[.*?\]\+', re.S), '', dictum)
        dictum = re.sub('\-.*?\+', '', dictum)
        dictum = re.sub('\s+', ' ', dictum)
        dictum = re.sub('^\s+', '', dictum) # remove leading whitespace characters
        dictum = re.sub('\s+$', '', dictum) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        if key in dictionary:
        # if there's already a dictionary entry with this key, merge the entries
            print('duplicate key: ' + key, file=sys.stderr)
            tmp = dictionary[key]
            dictum = tmp + ' ' + dictum
        dictionary[key] = dictum
    count = 1
    # uniq toc.txt > dedup.txt
    keys = tuple(open('./dedup.txt', 'r'))
    for key in keys:
        key = key.rstrip()
        print(key + '\n\n' + dictionary[key] + '\n')
        #
        # print('{:0=4}'.format(count) + ' _ ' + dictionary[key])
        # count = count + 1
        #
        # outfilename = './tmp/' + key + '.txt'
        # f = open(outfilename, 'w')
        # f.write(dictionary[key] + '\n')
        # f.close
        #

if __name__ == '__main__':
    main()
