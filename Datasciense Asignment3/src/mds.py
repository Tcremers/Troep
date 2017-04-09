# input:   1) datamatrix as loaded by numpy.loadtxt('dataset.txt')
#	   2) an integer d specifying the number of dimensions for the output (most commonly used are 2 or 3)
# output:  1) an N x d numpy array containing the d coordinates of the N original datapoints projected onto the top d PCs
#

import numpy as np
import matplotlib.pyplot as plt
import math
import pca


def main():
    trainInFilePath = "IDSWeedCropTrain.csv"
    dataTrain = np.loadtxt(trainInFilePath, delimiter = ",")
    centeredData = pca.centerDataMatrix(dataTrain)
    mdsMatrix = mds(centeredData, 2, 1)

def mds(data, dimensions, n):
    x = data[:, :-1]
    y = data[:, -1]
    dataMean = np.mean(data,0)
    sortedEvals, sortedEvecs, evals, evecs = pca.pca(data)
    c_var = np.cumsum(evals/np.sum(evals)) 

    #Perform mds
    mdsMatrix = np.zeros((dimensions,n,14))
    for d in range(dimensions):
        e = evecs[:,d]
        lambda1 = evals[d]
        std1 = np.sqrt(lambda1)
        valuesAlongPc = np.zeros((n,14))
        for i in range(n):
            valuesAlongPc[i,:] = dataMean + (i-3)*std1*e
        mdsMatrix[d] = valuesAlongPc    #Add data into one matrix
        
    #Plot the mds data
    fig, ax = plt.subplots()
    for matrix in mdsMatrix:
        print matrix
        for i in range(n):
            ax.plot(matrix[i])
    ax.set_title("Plot of n values of the Pesticide dataset \n onto the first d principal components.")
    plt.show()
    return mdsMatrix
        
def plotData(x,y):
    plt.plot(x,y)



if __name__ == '__main__':
    main()