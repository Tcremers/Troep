'''
Created on Mar 4, 2017

@author: Tycho

Introduction to Data sciense.
Assignment 2.
'''
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn import preprocessing

def main():
    trainInFilePath = "IDSWeedCropTrain.csv"
    testInFilePath = "IDSWeedCropTest.csv"
    xTrain, yTrain, xTest, yTest = getData(trainInFilePath, testInFilePath)
    
#     #Apply NN classifier with the default k: 1 and calculate accuracy of the model.
#     knn = applyNNClassifier(xTrain, yTrain)
#     accTest = accuracy_score(yTest, knn.predict(xTest))
#     print "Model accuracy value where k = " + str(1) + " :"
#     print accTest
#     
#     #Calculate Kbest
#     print"\nCalculating Kbest..."
#     kBest = getKbest(xTrain, yTrain)
#     print ""
#     
#     #Apply NN classifier with kBest, etc...
#     knn = applyNNClassifier(xTrain, yTrain, kBest)
#     accTest = accuracy_score(yTest, knn.predict(xTest))
#     print "Model accuracy value where k = " + str(kBest) + " :"
#     print accTest
#     
#     #Calculate Kbest again, but with the normalized data.
#     xTrainNorm, xTestNorm = normalizeData(xTrain, xTest)
#     print"\nCalculating Kbest..."
#     kBest = getKbest(xTrainNorm, yTrain)
#     print ""
#     #Apply NN classifier with new kBest and calculate accuracy with the normalized data.
#     knn = applyNNClassifier(xTrainNorm, yTrain, kBest)
#     accTest = accuracy_score(yTest, knn.predict(xTestNorm))
#     print "Model accuracy value where k = " + str(kBest) + " :"
#     print accTest
    
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
    print xTrain
    print yTrain
    
    xTest = dataTest[:, :-1]
    yTest = dataTest[:, -1]
    
    return xTrain, yTrain, xTest, yTest

def applyNNClassifier(x,y, k = 1):
    '''
    Apply a nearest neighbor classifier with sklearn.
    
    Key argument:
    x    :    matrix of data
    y    :    array of classifiers corresponding to x
    k    :    Number of neighbors to use by default for k_neighbors queries, default = 1
    '''
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x, y)
    return knn
    
def getKbest(xTrain, yTrain):
    '''
    Calculate the k that gives the highest accuracy for the given training data, using cross validation.
    
    Key arguments:
    xTrain    :    matrix of training data
    yTrain    :    array of classifiers corresponding to x
    '''
    
    kValues = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    cv = KFold(n_splits = 5)
    meanAccuracies = []
    
    for k in kValues:
        meanAccuracy = 0
        for train, test in cv.split(xTrain):
            xTrainCV, xTestCV, yTrainCV, yTestCV = xTrain[train], xTrain[test], yTrain[train], yTrain[test]
            knn = applyNNClassifier(xTrainCV, yTrainCV, k)
            accTest = accuracy_score(yTestCV, knn.predict(xTestCV))
            meanAccuracy += accTest
        meanAccuracy = meanAccuracy / 5
        meanAccuracies.append(meanAccuracy)
    accBest = max(meanAccuracies)
    kBest  = kValues[meanAccuracies.index(accBest)]
    
    print "All mean accuracies from cross validation: "
    print meanAccuracies
    print "Best accuracy: "
    print accBest
    print "Best k: "
    print kBest
    
    return kBest
    
    
def normalizeData(xTrain, xTest):
    '''
    Normalize the training and testing data using sklearn preprocessing
    
    Key arguments:
    xTrain    :    matrix of training data
    xTest    :    matrix of test data
    '''
    scaler = preprocessing.StandardScaler().fit(xTrain)
    xTrainNorm = scaler.transform(xTrain)
    xTestNorm = scaler.transform(xTest)
    
    return xTrainNorm, xTestNorm
    
    
    
if __name__ == '__main__':
    main()