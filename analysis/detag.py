#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
def main():
    file = open('./edF.txt', 'r').read()
    file = re.sub(re.compile('\-.*?\+', re.S), '', file)
    file = re.sub('\<.*?\>', '', file)
    # file = re.sub('\s+', ' ', file)
    file = re.sub('^\s+', '', file)
    file = re.sub('\s+$', '', file)
    print(file)

if __name__ == '__main__':
    main()
