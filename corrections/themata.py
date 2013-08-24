#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 19 March 2013
# 24 April 2013
#
# themata.py | fmt > themata.txt
#
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    count = 1
    themata = re.findall('\<2 \d{1,3}\>\<T Q\>(.*?)\<3 \d{1,2}\>', file, re.S)
    # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('36: ' + str(len(themata)))
    for thema in themata:
        thema = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', thema) # remove page and line number tags.
        thema = re.sub('\-.*?\+', '', thema)
        thema = re.sub('\s+', ' ', thema)
        thema = re.sub('^[ ]+', '', thema) # remove leading whitespace characters
        thema = re.sub('[ ]+$', '', thema) # remove trailing whitespace characters
        # print(thema + '\n')
        print('{:0=3}'.format(count) + ' _ ' + thema)
        count = count + 1

if __name__ == '__main__':
    main()
