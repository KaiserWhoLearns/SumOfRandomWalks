# Copyright ©2019 Kaiser Sun.
# This is a file for single random walk


# @para: n is the number of steps the whole walk is going to take
# steps is the possible choice of walks, must be a vector
# 10/06/2019
singleRandomWalk <- function(n, steps) {
    # Uncomment this line to get reproducilbe results
    # set.seed(1)
    walks <- cumsum(sample(steps, n, TRUE))
    return(walks)
}