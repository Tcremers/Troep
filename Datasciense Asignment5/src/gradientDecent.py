'''
Created on Mar 30, 2017

@author: Tycho

Data science asignment 5
Excercise 5
Ramdom forests
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import random


def main():
    #Source x from a random standard normal distribution as per de slide for lecture 12.
    x = np.random.normal(0, 1, 100)
    y = []
    
    #Calculate y with our function.
    for i in x:
        y.append(func(i))
#         y.append(derivativeFunction(i))

    #Select learningrate
#     learningrate = 0.1
    learningrate = 0.01
    learningrate = 0.001
    learningrate = 0.0001
    
    w, vals, iter = gradientDescent(1, learningrate)
    
    print "Results with learning rate " + str(learningrate) + ":"
    print "Final value = " + str(w)
    print "Number of iterations = " + str(iter)
    
    #Plot the gradient descent values.
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     ax.plot(vals)
    #Set the X axis according to how many values you plot to make the graph look a little better.
#     ax.set_xticks([0,1,2,3,4,5,6,7,8,9])
#     ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10])
#     plt.xlabel('Number of iterations')
#     plt.ylabel('Value of f')
#     plt.title("Plot of gradient descent steps with learning rate: " + str(learningrate))
#     plt.show()

    
    
def func(i):
    return math.exp(-(i/2)) + 10 * i**2

def derivativeFunction(i):
    print i
    return 20 * i - (math.exp(((0-i)/2))/2)


def gradientDescent(w, learningrate):
    value = 0
    # Setting parameters for convergence check
    num_iter = 1                   # This is the variable that will keep track of the number of iterations
    convergence = 0                # This is the variable that will keep track of whether we have converged
    max_iter = 10000              # We stop the algorithm after this many iterations
    tolerance = 1*10**-10          # We conclude convergence when the update difference in the objective function 
                                   # is less than the tolerance
    values = []                    # This variable will record the objective function value at each iteration. 
                                   # Not necessary (and takes up resources) but useful for insight when developing
                                   
    while convergence == 0:
        values.append(w)
        
        # Compute gradient and take a step in its direction
        grad = derivativeFunction(w)
#         print grad*learningrate                                                  
        w = w - learningrate*grad
        num_iter = num_iter + 1        
        
        # Checking for convergence
        diff = abs(value - w)
        value = w   
            
        if diff < tolerance:
            convergence = 1
        elif num_iter > max_iter:
            convergence = 1
    return w, values, num_iter




if __name__ == '__main__':
    main()