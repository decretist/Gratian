#!/bin/bash
for file in `cat manifest1`
do
  cat master/g1_$file.txt >> Gratian1.txt
done
for file in `cat manifest2`
do
  cat master/g2_$file.txt >> Gratian2.txt
done
