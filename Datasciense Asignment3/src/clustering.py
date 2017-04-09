'''
Created on Mar 12, 2017

@author: Tycho
Data sciense asignment 3
Exercise 3: K-means clustering
'''

import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans

def main():
    trainInFilePath = "IDSWeedCropTrain.csv"
    testInFilePath = "IDSWeedCropTest.csv"
    xTrain, yTrain, xTest, yTest = getData(trainInFilePath, testInFilePath)
    
    startingPoint = np.vstack((xTrain[0,], xTrain[1,]))
    print "Clustering..."
    kmeans = KMeans(2, n_init=1, init=startingPoint, algorithm='full' ).fit(xTrain)
    print "Done."
    
    print "Cluster centers: "
    print kmeans.cluster_centers_
    
def getData(trainInFilePath, testInFilePath):
    '''
    Retrieve the training and test data sets given the file paths to the training and test data files. 
    '''
    print "loading data...."
    #read in the data
    dataTrain = np.loadtxt(trainInFilePath, delimiter = ",")
    dataTest = np.loadtxt(testInFilePath, delimiter = ",")
    
    #split input variables and labels
    xTrain = dataTrain[:, :-1]
    yTrain = dataTrain[:, -1]
    
    xTest = dataTest[:, :-1]
    yTest = dataTest[:, -1]
    
    return xTrain, yTrain, xTest, yTest


if __name__ == '__main__':
    main()