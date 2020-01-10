#%%
import numpy as np
import matplotlib.pyplot as plt

# Generate a normal distributed random walk
# (Each step to be Normal(0, 1))
# @Para: numOfStep: total number of steps in one random walk
def single_random_walk(numOfStep):
    steps = np.random.normal(0, 1, numOfStep)
    walks = np.cumsum(steps, axis=0)
    return walks

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
            elif (argmax[0] == 0):
                # argmax at left endpoint
                res[1] += 1
            elif (argmax[0] == numOfStep - 1):
                # argmax at right endpoint
                res[3] += 1
    res /= numOfX * numOfY
    plt.plot(distribution)
    plt.show()
    res[0] = numOfY
    return res

if __name__== "__main__":
    ans = monteCarlo(10, 10000, 10000)
    print(ans)


# %%
