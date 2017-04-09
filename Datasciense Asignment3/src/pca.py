# input: datamatrix as loaded by numpy.loadtxt('dataset.txt')
# output:  1) the eigenvalues in a vector (numpy array) in descending order
#          2) the unit eigenvectors in a matrix (numpy array) with each column being an eigenvector (in the same order as its associated eigenvalue)
#
# note: make sure the order of the eigenvalues (the projected variance) is decreasing, and the eigenvectors have the same order as their associated eigenvalues
import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    trainInFilePath = "IDSWeedCropTrain.csv"
    testInFilePath = "IDSWeedCropTest.csv"
    murderDataInFilePath = "murderdata2d.txt"
    
    #Parse murder data
    murderData = np.loadtxt(murderDataInFilePath)
    #Center the data
    centeredMurderData = centerDataMatrix(murderData)
    #Perform PCA
    sortedEvals, sortedEvecs, evals, evecs = pca(centeredMurderData)
    #"2) the unit eigenvectors in a matrix (numpy array) with each column being an eigenvector"
    evecsAsCollumns = sortedEvecs.T
    #Create scatterplots
    plotPcaData(centeredMurderData, evals, evecs)
    plotPcaData(centeredMurderData, sortedEvals, sortedEvecs)
     
    
    #PCA for pesticide data
    dataTrain = np.loadtxt(trainInFilePath, delimiter = ",")
    centeredDataTrain = centerDataMatrix(dataTrain)
    sortedEvals, sortedEvecs, evals, evecs = pca(centeredDataTrain)
    evecsAsCollumns = sortedEvecs.T
    
    #plot of variance versus PC index
    c_var = np.cumsum(evals/np.sum(evals))
    fig, ax = plt.subplots()
    ax.plot(c_var)
    print c_var
    ax.set_title("Plot of variance versus PC index.")
    plt.show()

    
    
def pca(data):
    #Compute the covariance matrix
    covarianceMatrix = np.cov(data.T)
    #Compute eigenvalues and eigenvectors
    evals, evecs = np.linalg.eig(covarianceMatrix)
    sortedEvals = np.sort(evals)[::-1]
    sortedEvecs = np.array(evecs)
    #Sort eigenvalues and eigenvectors
    order = []
    for eval in sortedEvals:
        for i in range(len(evals)):
            if evals[i] == eval:
                order.append(i)
    for i in range(len(order)):
        sortedEvecs[i] = evecs[order[i]]
    return sortedEvals, sortedEvecs, evals, evecs
    
def plotPcaData(centeredData, evals, evecs):
    x = centeredData[:, :-1]
    y = centeredData[:, -1]
    
    fig, ax = plt.subplots()
    centeredDataMean = getMatrixMean(centeredData)
    ax.scatter(x, y, color = "blue")
    ax.axis('equal')
    ax.scatter(centeredDataMean[0], centeredDataMean[1] , color = "red", s = 100)
    s0 = np.sqrt(evals[0])
    s1 = np.sqrt(evals[1])
    
    ax.plot([0, s0*evecs[0,0]], [0, s0*evecs[1,0]], 'r')
    ax.plot([0, s1*evecs[0,1]], [0, s1*evecs[1,1]], 'r')
    ax.set_title('Scatter plot of PCA data with the mean(in red)\n and eigenvectors spanning from the mean.')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    plt.show()
    

def centerDataMatrix(dataMatrix):
    mean = np.mean(dataMatrix,0)
    centeredData = dataMatrix - mean
    return centeredData
    
def getMatrixMean(dataMatrix):
    return np.mean(dataMatrix,0)



if __name__ == '__main__':
    main()