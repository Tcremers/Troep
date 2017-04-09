'''
Created on Dec 5, 2016

@author: Tycho

Filling out a matrix with the nussinov algrorithm for a given RNA sequence.
'''
import Bio
import re


def main():
    sequence = "CGAUUGCA"
    scoreMatrix = []
    scoreMatrix = fillMatrix(sequence)
    
    print "Final matrix: "
    for vector in scoreMatrix:
        print vector
        
def fillMatrix(sequence):
    #baseMatrix = getBaseMatrix(sequence)
    scoreMatrix = getScoreMatrix(len(sequence))
    for base in range(2):
        for i in range(len(sequence)):
            for j in range(len(sequence)):
                if i < j:
                    baseRange = j-i
                    if baseRange > 1:
                        if scoreMatrix[i][j] <= scoreMatrix[i][j-1] and scoreMatrix[i][j] <= scoreMatrix[i+1][j-1] and scoreMatrix[i][j] <= scoreMatrix[i+1][j]:
                            if isBasePair(sequence[j] + sequence[j-baseRange]):
                                scoreMatrix[i][j] += 1
                            else:
                                scoreMatrix[i][j] = max(scoreMatrix[i][j-1],scoreMatrix[i+1][j])
    return scoreMatrix
        
def getScoreMatrix(sequenceLength):
    vector = []
    matrix = []
    for i in range(sequenceLength): 
        for j in range(sequenceLength):
            vector.append(0)
        matrix.append(vector)    
        vector = []
    return matrix

def getBaseMatrix(sequence):
    matrix = []
    vector = []
    for i in sequence:
        for j in sequence:
            vector.append(i+j)
        matrix.append(vector)
        vector = []
    return matrix


def isBasePair(pair):
    print pair
    basePairs = ["AU", "UA", "GC", "CG", "GU", "UG"]
    if pair.upper() in basePairs:
        return True
    return False
        
    
        
if __name__ == '__main__':
    main()