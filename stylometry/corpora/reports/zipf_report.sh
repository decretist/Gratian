#!/bin/bash
# Paul Evans (10evans@cua.edu)
# 13 February 2020
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bin\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bnon\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bet\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\best\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bquod\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bde\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bunde\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bad\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bqui\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bsed\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\buel\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\but\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bcum\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bautem\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bsi\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\ba\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bex\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bsunt\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\buero\b" | wc -l
cat ../corpus6/Gratian1.txt ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\benim\b" | wc -l
