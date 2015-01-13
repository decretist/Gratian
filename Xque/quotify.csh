#!/bin/csh
foreach word ( `cat schinke.txt`)
# foreach word ( `sort schinke.txt`)
echo "'"$word"'," >> quotified.txt
end
