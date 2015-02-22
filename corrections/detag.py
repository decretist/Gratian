#!/usr/bin/python
#
# Paul Evans (10evans@cardinalmail.cua.edu)
# 16 March 2013
#
# detag.py > detagged.txt
#
import re
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    file = re.sub(re.compile('\-.*?\+', re.S), '', file)
    file = re.sub(re.compile('\-\[.*?\]\+', re.S), '', file)
    file = re.sub('\<.*?\>', '', file)
    file = re.sub('[ ]+', ' ', file)
    file = re.sub(re.compile('[ ]$', re.MULTILINE), '', file)
    file = re.sub(re.compile('^[ ]', re.MULTILINE), '', file)
    file = re.sub('\n\n+', '\n', file)
    print(file)

if __name__ == '__main__':
    main()
