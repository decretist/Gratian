# Paul Evans (paul.evans@aya.yale.edu)
# 21 June 2019
#
setwd("~/Work/Gratian/stylometry/dash-q")
library(stylo)
#
files.to.analyze <- c("Gratian0-q.txt", "Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  use.custom.list.of.files = TRUE,
)
file.rename("wordlist.txt", "wordlist3.txt")
#
files.to.analyze <- c("Gratian0-q.txt", "Gratian1.txt", "Gratian2.txt","dePen1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  use.custom.list.of.files = TRUE,
)
file.rename("wordlist.txt", "wordlist4.txt")
