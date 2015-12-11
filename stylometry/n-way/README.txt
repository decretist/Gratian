2-way comparison of 1st- and 2nd-recension dicta:
Gratian1.txt (1st-recension dicta without de Pen.)
Gratian2.txt (2nd-recension dicta without de Pen.)
----------
3-way comparison of case statements, 1st-, and 2nd-recension dicta:
Gratian0.txt (vulgate case statements)
Gratian1.txt (1st-recension dicta without de Pen.)
Gratian2.txt (2nd-recension dicta without de Pen.)
----------
4-way comparison of case statements, 1st- and 2nd recension dicta,
    and 1st-recension dicta from de Pen.:
Gratian0.txt (vulgate case statements)
Gratian1.txt (1st-recension dicta without de Pen.)
Gratian2.txt (2nd-recension dicta without de Pen.)
dePen1.txt (1st-recension dicta from de Pen.)
----------
cd sample_dump
foreach file ( * )
cat "" >> $file
end
cat * > ../sample.txt
cd ..
vi sample.txt
:g/ /s//\r/gp
count.py | sort -k 1nr -k 2 | awk '{print $2}' | head -5000 > compare.txt
diff compare.txt wordlist.txt
(remember to edit wordlist.txt and delete the first 6 lines!)

