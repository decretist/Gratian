#!/bin/csh
cat input/Gratian[012].txt | false.py | sort -k 2 -n -r
