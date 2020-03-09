#!/bin/bash
cat ../corpus6/Gratian0.txt | while read line
do
  count=$(echo $line | wc -w)
  # echo $line $count
  echo $count
done
