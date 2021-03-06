#
# Paul Evans (decretist@gmail.com)
# 19 Mar 2020
#  7 Dec 2015
#
setwd("~/Work/Gratian/stylometry/n-way")
library(stylo)
#
# 3-way comparison of case statements, 1st-, and 2nd-recension dicta:
# Gratian0.txt (vulgate case statements)
# Gratian1.txt (1st-recension dicta without de Pen.)
# Gratian2.txt (2nd-recension dicta without de Pen.)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7a.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "3-way",
  custom.graph.filename = "3-way_PCA_51_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7a.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
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
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 49, mfw.max = 49,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "3-way",
  custom.graph.filename = "3-way_PCA_49_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
# 2-way comparison of 1st- and 2nd-recension dicta:
# Gratian1.txt (1st-recension dicta without de Pen.)
# Gratian2.txt (2nd-recension dicta without de Pen.)
#
files.to.analyze <- c("Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7c.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 53, mfw.max = 53,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1000,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "2-way",
  custom.graph.filename = "2-way_PCA_53_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
file.rename(
  from = "table_with_frequencies.txt",
  to = "Tukey/table_with_frequencies.txt"
)
#
files.to.analyze <- c("Gratian1.txt", "Gratian2.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = c("in", "non"),
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 2, mfw.max = 2,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "no.sampling", # default
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "technical",
  custom.graph.title = "2-way",
  custom.graph.filename = "2-way_PCA_2_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
# 4-way comparison of case statements, 1st- and 2nd recension dicta,
# and 1st-recension dicta from de Pen.:
# Gratian0.txt (vulgate case statements)
# Gratian1.txt (1st-recension dicta without de Pen.)
# Gratian2.txt (2nd-recension dicta without de Pen.)
# dePen1.txt (1st-recension dicta from de Pen.)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt", "dePen1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7d.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 49, mfw.max = 49,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "4-way",
  custom.graph.filename = "4-way_PCA_49_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
# 7 February 2016
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt", "dePen1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7d.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 49, mfw.max = 49,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "loadings",
  custom.graph.title = "4-way",
  custom.graph.filename = "4-way_PCA_49_MFWs_Loadings"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt", "Gratian2.txt", "dePen1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7e.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 46, mfw.max = 46,
  mfw.list.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "4-way",
  custom.graph.filename = "4-way_PCA_46_MFWs"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
# 5 July 2015
#
# 2-way comparison of case statements and 1st-recension dicta:
# Gratian0.txt (vulgate case statemeents)
# Gratian1.txt (1st-recension dicta without de Pen.)
#
files.to.analyze <- c("Gratian0.txt", "Gratian1.txt")
writeLines(files.to.analyze, "files_to_analyze.txt")
#
stylo.results = stylo(
  gui = FALSE,
  features = "wordlist7x.txt",
  corpus.dir = "../corpora/corpus7",
  corpus.lang = "Latin.corr",
  mfw.min = 51, mfw.max = 51,
  mfw.cutoff = 240,
  delete.pronouns = TRUE,
  use.custom.list.of.files = TRUE,
  analysis.type = "PCR",
  distance.measure = "delta",
  sampling = "normal.sampling",
  sample.size = 1200,
  write.jpg.file = TRUE,
  colors.on.graphs = "greyscale",
  pca.visual.flavour = "symbols",
  custom.graph.title = "Experimental",
  custom.graph.filename = "Experimental"
)
# summary(stylo.results)
print(stylo.results$features.actually.used)
#
file.rename(
  from = "table_with_frequencies.txt",
  to = "Tukey_x/table_with_frequencies.txt"
)
