#!/bin/csh
mallet import-dir --input data/gratian --output gratian-input.mallet --keep-sequence --stoplist-file stoplists/mgh.txt
mallet train-topics --optimize-interval 10 --num-topics 20 --num-iterations 1000 --input gratian-input.mallet --output-topic-keys gratian-20-topic-keys.txt --num-top-words 10
