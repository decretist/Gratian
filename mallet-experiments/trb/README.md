``` bash
./parse ../corrections/edF.txt > gratian.txt

mallet import-file --remove-stopwords  --keep-sequence \
  --input gratian.txt --output gratian.mallet \
  --stoplist-file ../stoplists/mgh.txt

mallet train-topics --num-threads 2 --input gratian.mallet \
  --num-topics 30 --optimize-interval 10 \
  --output-topic-keys gratian-30-keys.txt \
  --output-model gratian.model --num-top-words 10
```

