# Copyright ©2019 Kaiser Sun.
# This is a file for single random walk


# @para: n is the number of steps the whole walk is going to take
# steps is the possible choice of walks, must be a vector
# Returns the result of single random walks
# 10/06/2019
singleRandomWalk <- function(n, steps) {
    # Uncomment this line to get reproducilbe results
    # set.seed(1)
    walks <- cumsum(sample(steps, n, TRUE))
    return(walks)
}

# @para: n and steps are vars for singleRW
# times is the times of simulation we do
# Return the index where largest value happens
# 10/06/2019
massiveSimulation <- function(n, steps, times) {
    walks <- singleRandomWalk(n, steps)
    index <- match(max(walks), walks)
    result <- c(index)
    for (i in 2:times) {
        # remember that R vectors index starts at 1
        walks <- singleRandomWalk(n, steps)
        index <- match(max(walks), walks)
        result <- c(result, index)
    }
    return(result)
}