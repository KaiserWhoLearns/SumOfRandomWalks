#%%
import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures
import time

# Generate a normal distributed random walk
# (Each step to be Normal(0, 1))
# @Para: numOfStep: total number of steps in one random walk
def single_random_walk(numOfStep):
    steps = np.random.normal(0, 1, numOfStep)
    walks = np.cumsum(steps, axis=0)
    return walks

def single_random_walk_optimized(numOfStep, numOfX):
    steps = np.random.normal(0, 1, (2*numOfX, numOfStep))
    # print(steps)
    walks = np.cumsum(steps, axis=1)
    return walks

def monte_carlo_optimized(numOfStep, numOfX):
    walks = single_random_walk_optimized(numOfStep, numOfX)
    sums = np.add(walks[:numOfX, :], walks[numOfX:, :])

    sum_argmaxs = np.argmax(sums, axis=1)
    walks_argmaxs = np.argmax(walks[:numOfX, :], axis=1)
    print(np.count_nonzero(sum_argmaxs == 0))
    print(np.count_nonzero(sum_argmaxs == numOfStep - 1))
    print(np.count_nonzero(sum_argmaxs == walks_argmaxs))
    # plt.plot(walks_argmaxs)
    # plt.show()

# Do a Monte Carlo Simulation
# @Para: numOfX: the number of times generating X
# numOfY: nubmer of times generating Y for each X
# numOfStep: number of steps in one random walk
# return: (T(n), L(n), M(n), R(n)), where T(n) is numOfY
def monteCarlo(numOfX, numOfY, numOfStep):
    res = np.zeros(4)
    # distribution: the count of argmax happens at each index
    distribution = np.zeros(numOfStep)
    for i in range(0, numOfX):
        tempX = single_random_walk(numOfStep)
        for j in range(0, numOfY):
            sum = tempX + single_random_walk(numOfStep)
            argmax = np.where(sum == np.amax(sum))
            distribution[argmax] += 1
            if (np.where(tempX == np.amax(tempX)) == argmax):
                # argmax at X max
                res[2] += 1
            if (argmax[0] == 0):
                # argmax at left endpoint
                res[1] += 1
            if (argmax[0] == numOfStep - 1):
                # argmax at right endpoint
                res[3] += 1
    res /= numOfX * numOfY
    plt.plot(distribution)
    plt.show()
    res[0] = numOfY
    return res

if __name__ == "__main__":
    start = time.time()
    # # ans = monteCarlo(200000, 10, 1000)
    # res = np.zeros(4)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    #     # for i in range(0, 5):
    #     future = executor.submit(monteCarlo, 10000, 10, 1000)
    #     res += future.result()
    #     # print(res/5)
    # end = time.time()
    #monteCarlo(5,5,5)
    monte_carlo_optimized(1000, 100000)
    end = time.time()
    print(end - start)


# %%