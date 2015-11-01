#!/bin/bash
#
# Paul Evans
# 25 October 2015
#
if [ -f Gratian1.txt ];
then
    rm -i Gratian1.txt
fi
if [ -f Gratian2.txt ];
then
    rm -i Gratian2.txt
fi
while read -r line
do
    file=1r/$line.txt
    cat "$file" >> Gratian1.txt
done < toc_1r.txt
while read -r line
do
    file=2r/$line.txt
    cat "$file" >> Gratian2.txt
done < toc_2r.txt
shasum -c Gratian1.sha1
shasum -c Gratian2.sha1
