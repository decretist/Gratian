# Paul Evans (paul.evans@aya.yale.edu)
# 21 January 2019
#
setwd("~/Work/Gratian/stylometry/sg")
library(stylo)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt","dePen1.txt", "Gratian3.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  # "unde", "ergo", "igitur", and "quidem" occur in Sg but not Fr.
  # features = c("unde", "ergo", "igitur", "quidem"),
  features = "wordlist7sg.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 52, mfw.max = 52,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1000,
  write.jpg.file = TRUE,
  custom.graph.title = "Sg",
  custom.graph.filename = "Sg_PCA_52"
)
summary(stylo.results)
print(stylo.results$features.actually.used)
