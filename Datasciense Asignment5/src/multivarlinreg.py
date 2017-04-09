# input: 1) X: the independent variables (data matrix), an (N x D)-dimensional matrix, as a numpy array
#        2) y: the dependent variable, an N-dimensional vector, as a numpy array
#
# output: 1) the regression coefficients, a (D+1)-dimensional vector, as a numpy array
#
# note: remember to either expect an initial column of 1's in the input X, or to append this within your code

import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates.builtin_frames.utils import norm

def main():
    wineDataTrain = np.loadtxt("redwine_training.txt") 
#     wineDataTest = np.load("redwine_testing.txt")
    xTrain = wineDataTrain[:, :-1]
    yTrain = wineDataTrain[:, -1]
    
    #Only using the first feature
#     xTrain = wineDataTrain[:,:1]
    
    w = multivarlinreg(xTrain, yTrain)
    f = predictScores(xTrain, w)
    error = rmse(f, yTrain)
    print error
    
def multivarlinreg(x, y):
    # Append the data matrix with a column of ones
    num_pts = len(y)
    onevec = np.ones((num_pts,1))
#     print onevec
    x = np.concatenate((onevec, x), axis = 1)
    
    # Compute the regression coefficients
    w = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x), x)), np.transpose(x)), y)
    return w
    
def predictScores(x, w):
    wZero = w[0]
    w = np.array(w[1:])
    f = []
    for idx, wine in enumerate(x):
        score = wZero
        length = len(wine)
        for i in range(len(wine)):
            value = wine[i]*w[i]
            score += value
        f.append(score)
    return f
    
    
    
    
    
# input: 1) f: the predicted values of the dependent output variable, an N-dimensional vector, as a numpy array
#        2) t: the ground truth values of dependent output variable, an N-dimensional vector, as a numpy array
#
# output: 1) the root mean square error (rmse) as a 1 x 1 numpy array
def rmse(f, t):
    norms = []
    for i in range(len(f)):
        norm = np.square(abs(t[i] - f[i]))
        norms.append(norm)
    error = np.sum(norms) / len(f)
    error = np.sqrt(error)
    return error
    


if __name__ == '__main__':
    main()