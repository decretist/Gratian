#!/usr/local/bin/python3
import hashlib
import re

def tokenize(filename):
    '''open text file and return list of tokens'''
    text = open(filename, 'r').read().lower()
    tokens = [word for word in re.split('\W', text) if word != '']
    return tokens

def main():
    assert(
        hashlib.sha1(open('Gratian0.txt', 'rb').read()).hexdigest() ==
        '80b33a5ede195049ebb39d76a9b52c9314be2452'
    )
    assert(
        hashlib.sha1(open('Gratian1.txt', 'rb').read()).hexdigest() ==
        '5dc6dd1a83efbf85ea63e15539f1714db43bb84c'
    )
    assert(
        hashlib.sha1(open('Gratian2.txt', 'rb').read()).hexdigest() ==
        '62c0e13d63466caafa343bc5ece76fb2f24a8697'
    )
    assert(len(tokenize('Gratian0.txt')) == 3605)
    assert(len(tokenize('Gratian1.txt')) == 66238)
    assert(len(tokenize('Gratian2.txt')) == 14811)

if __name__ == '__main__':
    main()
