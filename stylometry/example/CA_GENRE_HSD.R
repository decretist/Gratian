###### LOAD DATA ###########################################################
library(ca)
library(languageR)
samples = read.table("~/Work/Gratian/stylo/example/dimensionReduction.tsv", header=TRUE)
samples.ca = ca(samples)
#plot(txts.ca, what=c("all", "none"))
meta = read.table("~/Work/Gratian/stylo/example/meta_data.tsv", header=TRUE)
COOR = data.frame(samples.ca$rowcoord, TEXT=meta$TEXT, GENRE=meta$GENRE)
############################################################################


print("######### FOR FIRST DIMENSION ##########################")
COOR.aov1 = aov(Dim1~GENRE, data=COOR)
print(TukeyHSD(COOR.aov1))
print(kruskal.test(COOR$Dim1, COOR$GENRE))
print("######### FOR SECOND DIMENSION ##########################")
COOR.aov2 = aov(Dim2~GENRE, data=COOR)
print(TukeyHSD(COOR.aov2))
print(kruskal.test(COOR$Dim2, COOR$GENRE))
############################################################################
###### TukeyHSD FOR POSITION VERSUS GENRE #########################
par(mfrow=c(1,2))
plot(TukeyHSD(COOR.aov1), sub=NULL)
abline(v=0, lty=3)
plot(TukeyHSD(COOR.aov2))
abline(v=0, lty=3)
par(mfrow=c(1,1))







