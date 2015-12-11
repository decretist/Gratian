# Paul Evans (decretist@gmail.com)
# 7 December 2015
#
setwd("~/Work/Gratian/stylometry/n-way")
library(stylo)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7a.txt",
  corpus.dir = "corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  custom.graph.title = "3-way",
  custom.graph.filename = "3-way_PCA_51_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7a.txt",
  corpus.dir = "corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  pca.visual.flavour = "loadings",
  custom.graph.title = "3-way",
  custom.graph.filename = "3-way_PCA_51_MFWs_Loadings"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7b.txt",
  corpus.dir = "corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 49, mfw.max = 49,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  custom.graph.title = "3-way",
  custom.graph.filename = "3-way_PCA_49_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
files.to.analyze <- c("Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7c.txt",
  corpus.dir = "corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 53, mfw.max = 53,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  sampling = "normal.sampling",
  sample.size = 1000,
  write.jpg.file = TRUE,
  custom.graph.title = "2-way",
  custom.graph.filename = "2-way_PCA_53_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
