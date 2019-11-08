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
source(paste0(Dir,'rwSimulationWeek7.R'), echo=TRUE)

# decrement/increment of step that we could choose
steps <- c(-1, 1)
# Steps we will do in a random walk
n <- 10000;
# Number of simulations
times <- 10000;

# the number of time where s(t) > 0 occurs
sim <- simulation2(n, steps, times, 1)

count = 0
for (i in 1 : length(sim)) {
  if (sim[i]) {
    count = count + 1
  }
}

