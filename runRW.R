# Copyright ©2019 Kaiser Sun.
# code to run random walks
# 10/06/2019
# need to be improved for visualization later
if(!require(ggplot2)) {
    install.packages("ggplot2")
}
library(ggplot2)

Dir<-"file:///Users/kaiser/Desktop/randomWalk/" 
# Change this to match the path for the folder you put the
source(paste0(Dir,'rwSimulation.R'), echo=TRUE)

# Simulation of first random walk
steps <- c(-1, 1)
n <- 10000;
walks <- c(singleRandomWalk(n, steps))
plotWalk <- data.frame(times = seq_along(walks), walks)
ggplot(plotWalk, aes(x = seq_along(walks), y = walks)) + geom_bar(stat = "identity")

# Now we want to sumulate a large number of times of RW
