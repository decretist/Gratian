#!/usr/local/bin/python3
#
# tags.py | egrep "<1 |<2 |<3 |<4 |<S |<T A>|<T P>|<T Q>|<T T>" > bones.txt
# fgrep "<S" bones.txt | sort -n -k 2 > tmp0
# uniq tmp0 > tmp1
# diff tmp0 tmp1 > dups.txt
#
import re
def main():
    this = last = ''
    f = open('./edF.txt', 'r')
    file = f.read()
    tags = re.findall(r'\<.*?\>', file)
    for tag in tags:
        m = re.match('\<S \d{1,4}\>', tag)
        if m:
            this = m.group()
            if (this == last):
                continue # duplicate detected
            last = this
        print(tag)

if __name__ == '__main__':
    main()
