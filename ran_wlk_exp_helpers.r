require(ramify)

random_walk <- function(length_n, step_size, prob=c(1/2, 1/2), lazy=FALSE) {
  res <- numeric(length_n)
  if (length_n > 1) {
    for(i in 2:length_n) {
      if(lazy) {
        step_i <- sample(c(step_size, 0, -step_size),1)
      } else {
        step_i <- sample(c(step_size,-step_size),1, prob = prob)
      }
      res[i] <- res[i-1] + step_i
    }
  }
  return(res)
}

experiment <- function(length_n, step_size, prob=c(1/2, 1/2), lazy=F, trials_n){
  res_walks <- list()
  for (i in 1:trials_n) {
    res_i <- random_walk(length_n, step_size, prob, lazy)
    res_walks[[i]] <- res_i
  }
  res_walks <- do.call(rbind, res_walks)
  return(res_walks)
}

#uses the index of the first max, bias towards start point
calc_argmax_prob <- function(res_matrix){
  total_num_trials <- dim(res_matrix)[1]
  # endpoint <- dim(res_matrix)[2]
  # midpoint <-round((1 + endpoint) / 2)
  
  argmax <- max.col(res_matrix)
  
  #indices_keep <- c(which(argmax == 1),
  #                   which(argmax == endpoint),
  #                   which(argmax == midpoint))
  # argmax[indices_keep] <- c("1_start_point","3_end_point", "2_middle_point")
  # argmax[-indices_keep] <- "4_other"
  #total_num_trials = 10
  res <- table(argmax)/total_num_trials
  
  #max <- apply(res_matrix[1:total_num_trials,], 1, max)
  #print(c("average max:", mean(max)))
  
  #df[, "max"] <- apply(df[, 2:26], 1, max)
  # max <- c()
  # for (i in 1:total_num_trials){
  #   max_i <- res_matrix[i,argmax[i]]
  #   max <- c(max, max_i)
  # }
  # 
  # res <- rbind(probability,max)
  return(res)
}

sum_prob_endpoints <- function(prob_res, wlk_length, num_trials) {
  average_middle <- mean(prob_res[-c(1,length(prob_res))])
  res <- c(prob_res[1], prob_res[round((1 + length(prob_res)) / 2)],  prob_res[length(prob_res)], average_middle, wlk_length, num_trials)
  names(res) <- c("start", "middle", "end", "average_middle", "wlk_length", "num_trials")
  return(res)
}

num_argmax <-  function(walk){
  max <- max(walk)
  res <- walk[which(walk == max)]
  return(length(res))
}
