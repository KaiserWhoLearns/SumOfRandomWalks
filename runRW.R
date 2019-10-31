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

# decrement/increment of step that we could choose
steps <- c(-1, 1)
# Steps we will do in a random walk
n <- 10000;
# Number of simulations
times <- 10000;

# Simulation of first random walk
# Uncomment it to see how a single random walk will look like
# walks <- c(singleRandomWalk(n, steps))
# plotWalk <- data.frame(seq_along(walks), walks)
# ggplot(plotWalk, aes(x = seq_along(walks), y = walks)) + geom_bar(stat = "identity")

# Now we count the number of maximum appears in each simulation
# maxStat <- countMax(n, steps, times)
# plotMaxStat <- data.frame(seq_along(maxStat), maxStat)
# length <- length(maxStat)
# Plot the max statistic

# Now we want to sumulate a large number of times of RW
sim <- massiveSimulation(n, steps, times)
plotSim <- data.frame(seq_along(sim), sim)
# Plot the count of each index
# This is the qplot one, not so cool
# qplot(sim, geom = "histogram", binwidth = 35, 
# main = "Count of largest indices", xlab = "Step of Walks", ylab = "Times Max Located")

# ggplot one, could change color for bars
ggplot(plotSim, aes(sim)) + geom_histogram(breaks=seq(1, n, by = 50), 
                 aes(fill=..count..)) +
  scale_fill_gradient("Count", low = "blue", high = "black") +
  xlab("Steps of Walk") + ylab("Distance walked") + 
  ggtitle("Maximum")

