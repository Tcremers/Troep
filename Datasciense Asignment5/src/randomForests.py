'''
Created on Mar 30, 2017

@author: Tycho

Data science asignment 5
Excercise 3 and 4
Ramdom forests
'''

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss


def main():
    xTrain, yTrain, xTest, yTest = getData("IDSWeedCropTrain.csv", "IDSWeedCropTest.csv")
    forest = RandomForestClassifier(50)
    forest.fit(xTrain,yTrain)
    
    forest_probs = forest.predict_proba(xTest)
    print forest_probs
    print "Accuracy: "
    print forest.score(xTest,yTest)
    
    

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