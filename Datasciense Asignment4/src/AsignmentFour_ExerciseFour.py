'''
Created on Mar 25, 2017

@author: Tycho
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():
    print "hello?"
    inFilePath = "IDSWeedCropTrain.csv"
    dataTrain = np.loadtxt(inFilePath, delimiter = ",")
    #split input variables and labels
    xTrain = dataTrain[:, :-1]
    yTrain = dataTrain[:, -1]
    
    #Get eigenvectors
    e1, e2 = doPca(xTrain)
    
    #Project the training data
    pcaTrainX = []
    pcaTrainY = []
    for vector in xTrain:
        x = np.dot(vector,e1)
        pcaTrainX.append(x)
        y = np.dot(vector ,e2)
        pcaTrainY.append(y)
    print len(pcaTrainX)
    print len(pcaTrainY)
    
    #Project the cluster centers
    clusterCenters = getClusterCenters(xTrain)
    pcaClusterX = []
    pcaClusterY = []
    for vector in clusterCenters:
        x = np.dot(vector,e1)
        pcaClusterX.append(x)
        y = np.dot(vector,e2)
        pcaClusterY.append(x)
    print pcaClusterX
    print pcaClusterY
    #Plot the data. Training data with rating 1 = red and 0 = Blue.
    for i, x in enumerate(pcaTrainX):
        if yTrain[i] == 1:
            plt.scatter(x, pcaTrainY[i], c = "red", s = 6)
        else:
            plt.scatter(x, pcaTrainY[i], c = "blue", s = 6)
            
    #The cluster centers are shown in orange
    plt.scatter(pcaClusterX, pcaClusterY, c = "Orange", s = 30)
    plt.title("The IDSweed training data and its 2 cluster centers projected\non it's first 2 PC.\nTraining data with rating 1 = red and 0 = Blue.\nCluster centers are orange ")
    plt.ylabel("Y axis", fontsize = 15)
    plt.xlabel("X axis", fontsize = 15)
    plt.show()
    
#     print yTrain


def getClusterCenters(xTrain):
    startingPoint = np.vstack((xTrain[0,], xTrain[1,]))
    print "Clustering..."
    kmeans = KMeans(2, n_init=1, init=startingPoint, algorithm='full' ).fit(xTrain)
    print "Done."
    
    print "Cluster centers: "
    return kmeans.cluster_centers_

def doPca(data):
    DataSigma = np.cov(data.T)
    evals, evecs = np.linalg.eig(DataSigma)
    e1 = evecs[:, 0]
    e2 = evecs[:, 1]
    return e1, e2
    vectorX = []
    













if __name__ == '__main__':
    main()