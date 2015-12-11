#!/usr/bin/python
#
# Paul Evans (decretist@gmail.com)
# 9 December 2015
#
# count.py | sort -k 1nr -k 2 | awk '{print $2}' | head -5000
#
from __future__ import print_function
import sys
def main():
    dictionary = {}
    sample = 'sample.txt'
    with open(sample, 'r') as f:
        words = f.readlines()
    words = [word.rstrip().lower().replace('v', 'u') for word in words]
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        if word not in dictionary:
            dictionary[word] = 1
    count = 0
    for word in dictionary.keys():
        count += dictionary[word]
        print(str(dictionary[word]) + '\t' + word)
    print(str(count) + ' words', file=sys.stderr)

if __name__ == '__main__':
    main()
