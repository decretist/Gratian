#!/bin/bash
#
# Paul Evans (10evans@cua.edu)
# 2 June 2020
#
if [ -f cases.txt ];
then
    rm -i cases.txt
fi
if [ -f laws.txt ];
then
    rm -i laws.txt
fi
if [ -f orders1.txt ];
then
    rm -i orders1.txt
fi
if [ -f orders2.txt ];
then
    rm -i orders2.txt
fi
if [ -f simony.txt ];
then
    rm -i simony.txt
fi
if [ -f procedure.txt ];
then
    rm -i procedure.txt
fi
if [ -f other1.txt ];
then
    rm -i other1.txt
fi
if [ -f other2.txt ];
then
    rm -i other2.txt
fi
if [ -f monastic.txt ];
then
    rm -i monastic.txt
fi
if [ -f other3.txt ];
then
    rm -i other3.txt
fi
if [ -f heresy.txt ];
then
    rm -i heresy.txt
fi
if [ -f marriage.txt ];
then
    rm -i marriage.txt
fi
if [ -f penance.txt ];
then
    rm -i penance.txt
fi
if [ -f second.txt ];
then
    rm -i second.txt
fi
while read -r line # C.1-36 d.init. (cases)
do
    file=../cases/$line.txt
    cat "$file" >> cases.txt
done < Contents/toc_cases.txt
while read -r line # R1 D.1-20 (laws)
do
    file=../1r/$line.txt
    cat "$file" >> laws.txt
done < Contents/toc_laws.txt
while read -r line # R1 D.21-80 (orders1)
do
    file=../1r/$line.txt
    cat "$file" >> orders1.txt
done < Contents/toc_orders1.txt
while read -r line # R1 D.81-101 (orders2)
do
    file=../1r/$line.txt
    cat "$file" >> orders2.txt
done < Contents/toc_orders2.txt
while read -r line # R1 C.1 (simony)
do
    file=../1r/$line.txt
    cat "$file" >> simony.txt
done < Contents/toc_simony.txt
while read -r line # R1 C.2-6 (procedure)
do
    file=../1r/$line.txt
    cat "$file" >> procedure.txt
done < Contents/toc_procedure.txt
while read -r line # R1 C.7-10 (other1)
do
    file=../1r/$line.txt
    cat "$file" >> other1.txt
done < Contents/toc_other1.txt
while read -r line # R1 C.11-15 (other2)
do
    file=../1r/$line.txt
    cat "$file" >> other2.txt
done < Contents/toc_other2.txt
while read -r line # R1 C.16-20 (monastic)
do
    file=../1r/$line.txt
    cat "$file" >> monastic.txt
done < Contents/toc_monastic.txt
while read -r line # R1 C.21-22 (other3)
do
    file=../1r/$line.txt
    cat "$file" >> other3.txt
done < Contents/toc_other3.txt
while read -r line # R1 C.23-26 (heresy)
do
    file=../1r/$line.txt
    cat "$file" >> heresy.txt
done < Contents/toc_heresy.txt
while read -r line # R1 C.27-36 (marriage)
do
    file=../1r/$line.txt
    cat "$file" >> marriage.txt
done < Contents/toc_marriage.txt
while read -r line # R1 and R2 de Penitentia (penance)
do
    file=../1r/$line.txt
    if [ -f "$file" ];
    then
        cat "$file" >> penance.txt
    fi
    file=../2r/$line.txt
    if [ -f "$file" ];
    then
        cat "$file" >> penance.txt
    fi
done < Contents/toc_penance.txt
while read -r line # R2
do
    file=../2r/$line.txt
    cat "$file" >> second.txt
done < Contents/toc_second.txt
shasum -c SHAs/cases.sha1
shasum -c SHAs/laws.sha1
shasum -c SHAs/orders1.sha1
shasum -c SHAs/orders2.sha1
shasum -c SHAs/simony.sha1
shasum -c SHAs/procedure.sha1
shasum -c SHAs/other1.sha1
shasum -c SHAs/other2.sha1
shasum -c SHAs/monastic.sha1
shasum -c SHAs/other3.sha1
shasum -c SHAs/heresy.sha1
shasum -c SHAs/marriage.sha1
shasum -c SHAs/penance.sha1
shasum -c SHAs/second.sha1
