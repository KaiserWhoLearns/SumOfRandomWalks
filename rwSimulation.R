# Copyright ©2019 Kaiser Sun.
# This is a file for single random walk


# @para: n is the number of steps the whole walk is going to take
# steps is the possible choice of walks, must be a vector
# Returns the result of single random walks
# 10/06/2019
singleRandomWalk <- function(n, steps) {
    # Uncomment this line to get reproducilbe results
 #    set.seed(1)
    walks <- cumsum(sample(steps, n, TRUE, prob = c(1, 1)))
    return(walks)
}

# @para: n and steps are vars for singleRW
# times is the times of simulation we do
# Return the index where largest value happens
# 10/06/2019
massiveSimulation <- function(n, steps, times) {
    walks <- singleRandomWalk(n, steps)
    walks <- matrix(walks, nrow = 1, ncol = length(walks))
    # index <- match(max(walks), walks)
    index <- max.col(walks)
    result <- c(index)
    for (i in 2:times) {
        # remember that R vectors index starts at 1
        walks <- singleRandomWalk(n, steps)
        walks <- matrix(walks, nrow = 1, ncol = length(walks))
        index <- max.col(walks)
        # index <- match(max(walks), walks)
        # index <- argmaxIndex(walks)
        result <- c(result, index)
    }
    return(result)
}

# Helper function, generate a ramdom indice of argmax
argmaxIndex <- function(walks) {
    argmax <- max(walks)
    indices <- match(argmax, walks)
    for (i in indices[1] + 1: length(walks)) {
        if (i > length(walks)) {
            break
        }
        if (walks[i] == argmax) {
            indices <- c(i, indices)
        }
    }
    # When length is 1, no need to take random
    if (length(indices) == 1) {
        return (indices)
    }
    # Pick a random index
    return (sample(indices, 1))
}

# @para: n and steps are vars for singleRW
# times is the times of simulation we do
# return the number of max appears in each simulation
# 10/17/2019
countMax <- function(n, steps, times) {
    walks <- singleRandomWalk(n, steps)
    count <- sum(max(walks)==walks)
    result <- c(count)
    for (i in 2:times) {
        # remember that R vectors index starts at 1
        walks <- singleRandomWalk(n, steps)
        count <- sum(walks == max(walks))
        result <- c(result, count)
    }
    frequent <- sum(result == 1)
    stat <- c(frequent)
    for (i in 2:max(result)) {
        frequent <- sum(result == i)
        stat <- c(stat, frequent)
    }
    return(stat)
}