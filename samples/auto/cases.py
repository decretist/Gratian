#!/usr/local/bin/python3
#
# Paul Evans (10evans@cua.edu)
# UCSD Biomedical Research Facility II
# 09 March 2020
#
import re
import sys
def main():
    file = open('../../analysis/edF.txt', 'r').read()
    toc = open('../hand/toc_cases.txt', 'r')
    dictionary_cases = {}
    # (?<=...) positive lookbehind assertion
    cases = re.findall('(?:\<T Q\>|(?<=\<T Q\>))(.*?)' # case statement starts with <T Q> tag
        # (?:...) non-capturing group
        '(?:'                   
            '\<3 1\>'
        # re.S (re.DOTALL) makes '.' special character match any character including newline
        ')', file, re.S)        
    print('expected 36 cases, found ' + str(len(cases)) + ' cases', file=sys.stderr)
    for case in cases:
        case = re.sub('\<S \d{1,4}\>\<L 1\>', '', case) # remove page and line number tags
        case = re.sub('\-.*?\+', '', case) # remove comment
        case = re.sub('\s+', ' ', case)
        case = re.sub('^\s+', '', case) # remove leading whitespace characters
        case = re.sub('\s+$', '', case) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        dictionary_cases[key] = case

    all = open('./Gratian0.txt', 'w')
    keys = tuple(open('../hand/toc_cases.txt', 'r'))
    for key in keys:
        key = key.rstrip()
        outfilename = './cases/' + key + '.txt'
        each = open(outfilename, 'w')
        each.write(dictionary_cases[key] + '\n')
        all.write(dictionary_cases[key] + '\n')
        each.close
    all.close()

if __name__ == '__main__':
    main()
