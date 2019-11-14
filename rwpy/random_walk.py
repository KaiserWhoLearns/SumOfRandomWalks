from random import randint
import numpy as np


def random_walk(trial_num, epoch):
    distributions = np.random.randint(1, 3, size=(trial_num, epoch))
    walks = np.where( distributions >= 2, 1, -1)
    walk_cumsums = np.cumsum(walks, axis=1)
    walk_cumsum_maxs = np.maximum.accumulate(walk_cumsums, axis=1)
    negative_walk_cumsum_max_counts = np.count_nonzero(walk_cumsum_maxs <= 0, axis=1)
    probability = np.count_nonzero(negative_walk_cumsum_max_counts > 0) / trial_num
    return probability

if __name__== "__main__":
    print(random_walk(10000, 10000))