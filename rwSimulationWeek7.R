# Copyright ©2019 Kaiser Sun.
# This is a file for single random walk

# @para: n is the number of steps the whole walk is going to take
# steps is the possible choice of walks, must be a vector
# Returns the result of single random walks
# 10/06/2019
singleRandomWalk <- function(n, steps) {
    # Uncomment this line to get reproducilbe results
 #    set.seed(1)
    walks <- cumsum(sample(steps, n, TRUE, prob = c(1, 3)))
    return(walks)
}

# j is the number of time where s(t) > 0 occurs
simulation2 <- function(n, steps, times, j) {
    walk <- singleRandomWalk(n, steps)
#    if (hasJos(walk, j)) {
#        result <- c(1)
#    } else {
    #    result <- c(0)
    # }
    result <- c(hasJPos(walk, j) && max(walk) == 0)
    for (i in 2 : times) {
        
        walk <- singleRandomWalk(n, steps)
        result <- c(result, hasJPos(walk, j) && max(walk) == 0)
    }
    return(result)
}

hasJPos <- function(walk, j) {
    count <- 0
    for (i in 1 : length(walk)) {
        if (walk[i] == 0) {
            count = count + 1
        }
    }
    return(count==j)
}