###### LOAD DATA ###########################################################
library(ca)
library(languageR)
samples = t(read.table("~/Work/Gratian/stylometry/3-way comparison/table_with_frequencies.txt", header=TRUE))
samples.ca = ca(samples)
#plot(txts.ca, what=c("all", "none"))
meta = read.table("~/Work/Gratian/stylometry/3-way comparison/meta_data.tsv", header=TRUE)
COOR = data.frame(samples.ca$rowcoord, TEXT=meta$TEXT)
############################################################################

print("######### FOR FIRST DIMENSION ##########################")
COOR.aov1 = aov(Dim1~TEXT, data=COOR)
print(TukeyHSD(COOR.aov1))
print(kruskal.test(COOR$Dim1, COOR$TEXT))
print("######### FOR SECOND DIMENSION ##########################")
COOR.aov2 = aov(Dim2~TEXT, data=COOR)
print(TukeyHSD(COOR.aov2))
print(kruskal.test(COOR$Dim2, COOR$TEXT))
############################################################################
###### TukeyHSD FOR POSITION VERSUS TEXT #########################
par(mfrow=c(1,2))
plot(TukeyHSD(COOR.aov1), sub=NULL)
abline(v=0, lty=3)
plot(TukeyHSD(COOR.aov2))
abline(v=0, lty=3)
par(mfrow=c(1,1))
