#!/bin/bash
if [ -f Gratian1.txt ];
then
  rm -i Gratian1.txt
fi
if [ -f Gratian2.txt ];
then
  rm -i Gratian2.txt
fi
for file in `cat manifest1`
do
  cat master/g1_$file.txt >> Gratian1.txt
done
for file in `cat manifest2`
do
  cat master/g2_$file.txt >> Gratian2.txt
done
shasum -c Gratian1.sha1
shasum -c Gratian2.sha1

