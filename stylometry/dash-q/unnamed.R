# Paul Evans (paul.evans@aya.yale.edu)
# 21 June 2019
setwd("~/Work/Gratian/stylometry/dash-q")
library(stylo)
#
files.to.analyze <- c("Gratian0-q.txt", "Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = TRUE,
  features = "wordlist7q3.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 300,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1600,
  write.jpg.file = TRUE,
  custom.graph.title = "No questions, 3-way",
  custom.graph.filename = "NoQ_PCA_3"
)
summary(stylo.results)
print(stylo.results$features.actually.used)
#
files.to.analyze <- c("Gratian0-q.txt", "Gratian1.txt", "Gratian2.txt","dePen1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = TRUE,
  features = "wordlist7q4.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 300,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1600,
  write.jpg.file = TRUE,
  custom.graph.title = "No questions, 4-way",
  custom.graph.filename = "NoQ_PCA_4"
)
summary(stylo.results)
print(stylo.results$features.actually.used)
