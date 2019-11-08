# Try to calculate the convergence of the Markov Chain result
from numpy import matrix
from numpy.linalg import matrix_power
import math

n = 10000
S = matrix([[0.5, 0.5, -2 / math.sqrt(3), 2/math.sqrt(3)],
[0.25, 0.75, 1, 1],
[0, 1, 0, 0],
[1, 0, 0, 0]])
J = matrix([[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, -1/math.sqrt(3), 0],
[0, 0, 0, 1/math.sqrt(3)]])
sInverse = matrix([[0, 0, 0, 1], [0, 0, 1, 0],
[-math.sqrt(3)/4, 0.5, math.sqrt(3)/4*(0.5 - math.sqrt(3)/2), math.sqrt(3)/4*(0.5 - 1/(2*math.sqrt(3)))],
[math.sqrt(3)/4, 0.5, math.sqrt(3)/4*(-0.5 - math.sqrt(3)/2), math.sqrt(3)/4*(-0.5 - 1/(2*math.sqrt(3)))]])
start = matrix([[1], [0], [0], [0]])
start2 = matrix([1, 0, 0, 0])
print S*matrix_power(J, n)*sInverse*start
print start2*S*matrix_power(J, n)*sInverse

print "Jordan mult"
print S*matrix_power(J, n)*sInverse

A = matrix([[0, 2.0/3.0, 0, 1.0/3.0], [0.5, 0, 0.5, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
print matrix_power(A, n)*start