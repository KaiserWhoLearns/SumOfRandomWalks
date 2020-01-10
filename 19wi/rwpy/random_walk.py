from random import randint
import numpy as np


def random_walk(trial_num, epoch):
    distributions = np.random.randint(1, 4, size=(trial_num, epoch))
    walks = np.where( distributions >= 2, 1, -1)
    walk_cumsums = np.cumsum(walks, axis=1)
    walk_cumsum_maxs = np.maximum.accumulate(walk_cumsums, axis=1)
    negative_walk_cumsum_max_counts = np.count_nonzero(walk_cumsum_maxs <= 0, axis=1)
    probability = np.count_nonzero(negative_walk_cumsum_max_counts > 0) / trial_num
    return probability


def single_random_walk(epoch):
    distributions = np.random.randint(1, 3, size=(1, epoch))
    # distributions = np.random.randint(1, 3, size=(10, 10))
    walks = np.where( distributions >= 2, 1, -1)
    walk_cumsums = np.cumsum(walks, axis=1)
    return walk_cumsums
    
def sum_random_walk(trial, X, epoch):
    # Count the number of maximum appears at each index
    count = np.full_like(X[0], 0)
    # For loop, sum up to see where the maximum locates
    for i in range(0, trial):
        Y = single_random_walk(epoch)
        twosum = X + Y
        # Record the maximum in the array
        max_value_indices = np.where(twosum == np.amax(twosum))
        for index in max_value_indices:
            count[index] += 1
    return np.where(count == np.amax(count))

        


if __name__== "__main__":
    # Genderate a randomwalk X
    X = single_random_walk(200)
    print("The known random walk")
    print(X[0][0])
    # print(np.where(X == np.amax(X[0][0])))
    # Sum up the random walk
    print("Where maximums happens most: ")
    print(sum_random_walk(200, X, 200))
    # print(random_walk(10000, 10000))
    # Try doing maximum likelyhood estimation