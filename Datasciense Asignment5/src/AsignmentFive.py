'''
Created on Mar 30, 2017

@author: Tycho
'''
import numpy as np


def main():
    print "hello world"
    wineDataTrain = np.load("redwine_training.txt") 
    wineDataTest = np.load("redwine_testing.txt")
    
    sepalTrain = np.load("Iris2D2_train.txt")
    sepalTest = np.load("Iris2D2_test.txt")
    
    petalTrain = np.load("Iris2D1_train.txt")
    petalTest = np.load("Iris2D1_test.txt")

    
    
if __name__ == '__main__':
    main()