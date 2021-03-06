setwd(normalizePath(dirname(R.utils::commandArgs(asValues=TRUE)$"f")))
source('../findNSourceUtils.R')

test.rdoc_table.golden <- function(H2Oserver) {

prosPath = system.file("extdata", "prostate.csv", package="h2o")
prostate.hex = h2o.importFile(H2Oserver, path = prosPath, key = "prostate.hex")
summary(prostate.hex)
head(h2o.table(prostate.hex[,3]))
head(h2o.table(prostate.hex[,c(3,4)]))

testEnd()
}

doTest("R Doc Table", test.rdoc_table.golden)

