#!/bin/bash
#
# Paul Evans
# UCSD Biomedical Research Facility II
# 09 March 2020
#
if [ -f Gratian0.txt ];
then
    rm -i Gratian0.txt
fi
if [ -f Gratian1.txt ];
then
    rm -i Gratian1.txt
fi
if [ -f Gratian2.txt ];
then
    rm -i Gratian2.txt
fi
if [ -f dePen1.txt ];
then
    rm -i dePen1.txt
fi
if [ -f dePen2.txt ];
then
    rm -i dePen2.txt
fi
while read -r line
do
    file=../cases/$line.txt
    cat "$file" >> Gratian0.txt
done < toc_cases.txt
while read -r line
do
    file=../1r/$line.txt
    cat "$file" >> Gratian1.txt
done < toc_1r.txt
while read -r line
do
    file=../2r/$line.txt
    cat "$file" >> Gratian2.txt
done < toc_2r.txt
while read -r line
do
    file=../1r/$line.txt
    cat "$file" >> dePen1.txt
done < toc_dP1.txt
while read -r line
do
    file=../2r/$line.txt
    cat "$file" >> dePen2.txt
done < toc_dP2.txt
shasum -c Gratian0.sha1
shasum -c Gratian1.sha1
shasum -c Gratian2.sha1
shasum -c dePen1.sha1
shasum -c dePen2.sha1
