#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
import sys
def main():
    string = sys.stdin.read()
    words = re.split('\W', string)
    for word in words:
        if word.endswith('ne'):
            print(word)

if __name__ == '__main__':
    main()
