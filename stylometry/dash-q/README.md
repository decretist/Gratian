# dash-q

This directory needs to be merged into ```n-way``` when finished.

### Checklist

- [x] ```cp -i -p Gratian/samples/hand/Gratian0-q.txt Gratian/stylometry/corpora/corpus6/```  
Map _-que_ enclitic to pseudo-conjunction _xque_:
- [x] ```cp -i -p Gratian/samples/hand/Gratian0-q.txt Gratian/Xque/input```
- [x] ```(cd Gratian/Xque; xque.py < input/Gratian0-q.txt > output/Gratian0-q.txt)```  
(Only one occurrence, _eamque_ in C.29 d.init.)
- [x] ```cp -i -p Gratian/Xque/output/Gratian0-q.txt Gratian/stylometry/corpora/corpus7```
