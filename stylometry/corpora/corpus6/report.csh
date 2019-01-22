#!/bin/csh
cat Gratian1.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bin\b" | wc -l
cat Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bin\b" | wc -l
cat Gratian1.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bnon\b" | wc -l
cat Gratian2.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | egrep "\bnon\b" | wc -l
