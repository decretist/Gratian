#!/usr/bin/python
#
# Paul Evans
# 4 May 2015
#
# Usage: cat input/Gratian?.txt | ../false_positives.py | sort -k 2 -n -r
#
import re
import sys
# http://snowball.tartarus.org/otherapps/schinke/intro.html
ignore = ['atque', 'quoque', 'neque', 'itaque', 'absque', 'apsque',
    'abusque', 'adaeque', 'adusque', 'denique', 'deque', 'susque',
    'oblique', 'peraeque', 'plenisque', 'quandoque', 'quisque',
    'quaeque', 'cuiusque', 'cuique', 'quemque', 'quamque', 'quaque',
    'quique', 'quorumque', 'quarumque', 'quibusque', 'quosque',
    'quasque', 'quotusquisque', 'quousque', 'ubique', 'undique',
    'usque', 'uterque', 'utique', 'utroque', 'utribique', 'torque',
    'coque', 'concoque', 'contorque', 'detorque', 'decoque',
    'excoque', 'extorque', 'obtorque', 'optorque', 'retorque',
    'recoque', 'attorque', 'incoque', 'intorque', 'praetorque',
    'que']
# false positives in case statements, 1st-, and 2nd-recension dicta
false = ['cumque', 'eque', 'namque', 'pleraque', 'plerique',
    'plerisque', 'plerumque', 'quinque', 'unamquamque', 'unaqueque',
    'unicuique', 'uniuscuiusque', 'unumquemque', 'unusquisque',
    'usquequaque', 'utramque', 'utraque', 'utrique', 'utrisque',
    'utriusque', 'utrumque']
def main():
    # dictionary of false positives
    dictionary ={}
    for entry in false:
        dictionary[entry] = 0
    string = sys.stdin.read()
    words = re.split('\W', string)
    for word in words:
        cumque = re.match(r'(\w+)cu[mn]que(?:\b)', word)
        que = re.match(r'(\w+)que(?:\b)', word)
        if que:
            if word.lower() not in ignore:
                if not cumque:
                    if word.lower() not in false:
                        pass
                    else:
                        dictionary[word.lower()] += 1
                else:
                    pass
            else:
                pass
        else:
            pass
    keys = dictionary.keys()
    for key in keys:
        print(key + ': ' + str(dictionary[key]))

if __name__ == '__main__':
    main()
