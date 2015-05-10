#!/bin/csh
#
# Paul Evans
# 4 May 2015
#
echo 'total occurrences of que:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bque\b" | wc -l
echo 'total occurrences of -que:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\b[a-zA-Z]+que\b" | wc -l
echo 'unique occurrences of -que:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\b[a-zA-Z]+que\b" | sort | uniq | wc -l
echo 'total occurrences of cumque:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bcumque\b" | wc -l
echo 'total occurrences of -cu[mn]que:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\b[a-zA-Z]+cu[mn]que\b" | wc -l
echo 'unique occurrences of -cu[mn]que:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\b[a-zA-Z]+cu[mn]que\b" | sort | uniq | wc -l
#
echo 'nam:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bnam\b" | wc -l
echo 'namque:'
cat ./input/Gratian?.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bnamque\b" | wc -l
#
echo 'in (Gratian 1):'
cat ./input/Gratian1.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bin\b" | wc -l
echo 'in (Gratian 2):'
cat ./input/Gratian2.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bin\b" | wc -l
echo 'non (Gratian 1):'
cat ./input/Gratian1.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bnon\b" | wc -l
echo 'non (Gratian 2):'
cat ./input/Gratian2.txt | tr -d '[:punct:]' | tr '[:space:]' '\n' | egrep -v '^$' | tr '[:upper:]' '[:lower:]' | egrep "\bnon\b" | wc -l
#
echo 'total occurrences of -que not in Schinke pass list:'
cat ./output/Gratian?.txt | tr '[:upper:]' '[:lower:]' | grep xque | wc -l
echo 'unique occurrences of -que not in Schinke pass list:'
cat ./output/Gratian?.txt | tr '[:upper:]' '[:lower:]' | grep xque | sort | uniq | wc -l
