'''
Created on Mar 22, 2017

@author: Tycho
'''
import matplotlib.pyplot as plt
import numpy as np
import math
from comtypes.npsupport import numpy
from astropy.units import one

def main():
    print "hello world!"
    data = np.loadtxt("diatoms.txt")
    x = data[0][0::2]
    y = data[0][1::2]
    plt.plot(x,y)
    plt.axis("equal")
    plt.show()
    #Plot all cells.
    plotCells(data) 

    doCellPca(data)
    toyData = data = np.loadtxt("pca_toydata.txt")
#     print toyData
    doToyDataPca(toyData)
    for toy in toyData:
        x = toy[0::2]
        y = toy[1::2]
        plt.scatter(x,y)
    plt.title("Plot of the raw toydata")
    plt.show()
    plt.axis("equal")
    
def doToyDataPca(toyData):
    DataSigma = np.cov(toyData.T)
    evals, evecs = np.linalg.eig(DataSigma)
    m  = getMean(toyData)
    e1 = evecs[:, 0]
    e2 = evecs[:, 1]
    
    vectorX = []
    vectorY = []
    
    for toy in toyData:
        x = np.dot(toy,e1)
        y = np.dot(toy,e2)
        vectorX.append(x)
        vectorY.append(y)
    
    plt.scatter(vectorX,vectorY)
    plt.title("Plot of the first two PC's projected on the toydata.")
    plt.show()

    o1 = np.sqrt(evals[0])
    o2 = np.sqrt(evals[1])

def doCellPca(data):
    DataSigma = np.cov(data.T)
    evals, evecs = np.linalg.eig(DataSigma)
    m  = getMean(data)

    e1 = evecs[:, 0]
    e2 = evecs[:, 1]
    e3 = evecs[:, 2]
    o1 = np.sqrt(evals[0])
    o2 = np.sqrt(evals[1])
    o3 = np.sqrt(evals[2])
    
    one = [m-2*o1*e1, m-o1*e1, m, m+o1*e2, m+2*o1*e1]
    two = [m-2*o2*e2, m-o2*e2, m, m+o2*e2, m+2*o2*e2]
    three = [m-2*o3*e3, m-o3*e3, m, m+o3*e2, m+2*o3*e3]
    
    plotCells(one, "Plot of 5 cells coresponing to first principal component.")
    plotCells(two, "Plot of 5 cells coresponing to second principal component.")
    plotCells(three, "Plot of 5 cells coresponing to third principal component.")
    
    
def plotCells(data, title = "Plot of cells"):
    for cell in data:    
        x,y = getVectors(cell)
        plt.plot(x,y)
    plt.title(title)
    plt.ylabel("Y-axis")
    plt.xlabel("X-axis")
    plt.axis("equal")
    plt.show()
    
def getMean(data):
    l = len(data[0])
    total = numpy.zeros(l)
    for cell in data:
        total += cell 
    mean = total / l
    
    return mean
        
def getVectors(cell):
    x = cell[0::2]
    y = cell[1::2]
    return x,y

def getData(filePath):
    return None 



if __name__ == '__main__':
    main()