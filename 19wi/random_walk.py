#%%
import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures
import time
from scipy.optimize import curve_fit
from math import sqrt
from collections import Counter

# Generate a normal distributed random walk
# (Each step to be Normal(0, 1))
# @Para: numOfStep: total number of steps in one random walk
def single_random_walk(numOfStep):
    steps = np.random.normal(0, 1, numOfStep)
    walks = np.cumsum(steps, axis=1)
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

# This is for week10, when we try to fix a special X, and see its trend for Y
def monte_carlo_fixX(numOfStep, X, numOfY):
    Y = single_random_walk_optimized(numOfStep, int(numOfY / 2))
    sums = np.add(Y[:, :], X)
    sum_argmaxs = np.argmax(sums, axis=1)
    X_argmax = np.argmax(X, axis=0)
    sum_argmaxs_minus_X_argmax = np.abs(np.subtract(sum_argmaxs, X_argmax))
    counts = Counter(sum_argmaxs_minus_X_argmax)
    lists = sorted(counts.items())
    x, y = zip(*lists)
    # Loop
    ynew = np.zeros(numOfStep + 1)
    for i in range(0, len(x)):
        ynew[x[i]] = y[i]
    return ynew
    # print(x)
    # print(y)
    # plt.plot(x, y)
    # plt.show()

    
######### Below is the functions for curve-fitting #######
def exp(x, a, b, c):
    return a * np.exp(-b * x) + c

def exp2(x, a, b):
    return a * np.exp(-b * x)

def exp3(x, a, b, c):
    return a * np.power(x + c, b)

def invp(x, a):
    return a / x

# The argmax(X) = numOfStep / 2 in this case
# The maximum value is sqrt(n)
def specialXSimulation(numOfStep, numOfY, c):
    X = np.zeros(numOfStep)
    # Generate our special X
    for i in range(0, int(numOfStep/2)):
        X[i] = c * sqrt(i)
    for i in range(int(numOfStep/2), numOfStep):
        X[i] = 2 * c * sqrt(numOfStep) - 2 * c * i / sqrt(numOfStep)
    # Start simulation
    count = monte_carlo_fixX(numOfStep, X, numOfY) # y-axis
    difference = np.arange(numOfStep + 1) # x-axis
    # Original plot
    plt.plot(difference, count, 'b-', label="original plot")
    # Exponential fit3
    popt_exp3, pcov_exp3 = curve_fit(exp3, difference, count)
    print("Exponential fit3 parameters: ", popt_exp3)
    plt.plot(difference, exp3(difference, *popt_exp3), 'g--', label="exponential fit")
    # Exponential fit2
    popt_exp2, pcov_exp2 = curve_fit(exp2, difference, count)
    print("Exponential fit2 parameters: ", popt_exp2)
    plt.plot(difference, exp2(difference, *popt_exp2), 'r--', label="exponential fit2")
    # # Polynomial fit
    # popt_invp, pcov_invp = curve_fit(invp, difference, count)
    # print("Inversely Propotional fit parameters: ", popt_invp)
    # plt.plot(difference, invp(difference, *popt_invp), 'r-', label="inversely proportional fit")
    plt.show()


## Plotting functions ##
def plot_num_of_x_vs_num_of_max(max_iteration, steps, unit):
    result = [monte_carlo_optimized(steps, iteration) for iteration in range(1, max_iteration, unit)]
    plt.plot(range(1, max_iteration, unit), result)
    plt.title('number of sum argmax of sum vs iterations with steps = ' + str(steps))
    plt.xlabel('iterations')
    plt.ylabel('number of sum argmax')
    plt.legend(['argmaxSum=0', 'argmaxSum=numOfStep-1', 'argmaxSum=argmaxX'], loc='best')
    plt.show()
    #plt.savefig("temperature_at_christmas.pdf")

def plot_num_of_step_vs_probability(iteration, max_steps, unit):
    result = [np.divide(monte_carlo_optimized(steps, iteration), float(iteration)) for steps in range(1, max_steps, unit)]
    plt.plot(range(1, max_steps, unit), result)
    plt.title('number of steps vs iterations with iteration = ' + str(iteration))
    plt.xlabel('steps')
    plt.ylabel('probability')
    plt.legend(['argmaxSum=0', 'argmaxSum=numOfStep-1', 'argmaxSum=argmaxX'], loc='best')
    plt.show()


########## Below is an archived function of MonteCarlo Simulation, which is slow ########
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
    # monteCarlo(5,5,5)
    # monte_carlo_optimized(1000, 1000000)
    specialXSimulation(10000, 100000, 1)
    end = time.time()
    print("Time used: ", end - start, "seconds")


# %%