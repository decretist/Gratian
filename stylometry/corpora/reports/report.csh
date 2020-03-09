#!/bin/csh
cat ../corpus6/Gratian1.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bin\b" | wc -l
cat ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bin\b" | wc -l
cat ../corpus6/Gratian1.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bnon\b" | wc -l
cat ../corpus6/Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bnon\b" | wc -l
