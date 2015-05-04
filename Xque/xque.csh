#!/bin/csh
#
# Paul Evans
# 4 May 2015
#
foreach n ( 0 1 2 )
echo "Gratian$n.txt"
    xque.py < input/Gratian$n.txt > output/Gratian$n.txt
end
