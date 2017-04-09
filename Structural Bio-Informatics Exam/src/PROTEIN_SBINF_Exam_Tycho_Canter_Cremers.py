'''
Created on Jan 24, 2017

@author: Tycho
Structural Bio-informatics Exam
Protein part.
'''
import os
import Bio.PDB as pdb
import inspect
import numpy
import itertools


def main():
    pairLength = 5
    inFolder = "\\top100H"      #Folder containing top100 files pdb files
#     inFolder = "\\randomProteins"      #Folder containing 200 random pdb files
#     inFolder = "\\test"      #Test folder containing only a few specific pdb files
    topPairDict = getSequencePairs(inFolder, pairLength)
    topRMSDvalueList = getRmsdValues(topPairDict)
    
    
    inFolder = "\\randomProteins"      #Folder containing 200 random pdb files
    randomPairDict = getSequencePairs(inFolder, pairLength)
    randomRMSDvalueList = getRmsdValues(randomPairDict)
    
    print "Top 100: "
    print "Found " + str(len(topPairDict)) + " sequences that occur in two or more proteins"
    print "RMSD Value count: " + str(len(topRMSDvalueList))
    print topRMSDvalueList
    print "Random: "
    print "Found " + str(len(randomPairDict)) + " sequences that occur in two or more proteins from "
    print "RMSD Value count: " + str(len(randomRMSDvalueList))
    print randomRMSDvalueList[0:len(topRMSDvalueList)]
    
def getSequencePairs(inFolder, pairLength):
    '''
    Gather all sequences of length n that occur in 2 or more files, given a foler containing PDB files.
    
    Key arguments:
    inFolder : str
        A folder or path to a folder in the current working directory, containing pdb files.
    pairLength : int
        Length of the sequences you want to find all possible pairs for.
    '''
    
    aminoAcidDict = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W', 
     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}
    pairDict = {}
    parser = pdb.PDBParser()
    fileCount = 0
    inFolder = os.getcwd() + inFolder
    logFile = open("logFile.txt", "w")
    for fileName in os.listdir(inFolder):       #Iterate over all files in given folder
        filePath = inFolder + "\\" + fileName
        fileCount += 1
                                  
        print "Parse file: " + fileName
        try:                                    #Try block for structure parser to catch pdb files that give an error.
            structure = parser.get_structure(fileCount, filePath)
        except ValueError as e:
            logFile.write("Error in file: \"" + fileName + "\" Error: " + e.message + "\n")     #Log error to logfile and skip file.
            continue
        print "Done parsing: " + fileName
        
        residueCount = 0
        sequenceKey = ""
        sequenceValue = []
        
        for residue in structure.get_residues():    #Iterate over all residues.
            if pdb.is_aa(residue):                  #Check if it's actually an amino acid.
                if residue.get_resname() not in aminoAcidDict or "CA" not in residue:  #Check if it's not some exotic aa,
                    residueCount = 0
                else:                               
                    aa = aminoAcidDict[residue.get_resname()]
                    if residueCount < pairLength:   #Start filling an n-length sequence.
                        sequenceKey += aa
                        sequenceValue.append(residue)
                        residueCount += 1
                    else:                           #Add n-length sequences to dictionary. Key is one-letter sequence, value is array of residue objects.
                        if sequenceKey in pairDict:
                            if fileCount not in pairDict[sequenceKey]:
                                for key, val in pairDict[sequenceKey].items():
                                    if val[0].get_id()[1] != sequenceValue[0].get_id()[1]:      #If residue positions are the same chances are high we're storing pairs of the same protein. And so we ignore those.
                                        pairDict[sequenceKey][fileCount] = sequenceValue        #Separate values by what file they came from to not add duplicates from the same file.
                        else:
                            pairDict[sequenceKey] = { fileCount : sequenceValue}
                        sequenceKey = sequenceKey[1:pairLength] + aa        #Omit first index of sequences and add next residue.
                        sequenceValue = sequenceValue[1:pairLength]
                        sequenceValue.append(residue)
                        
    pruneNonePairs(pairDict)
    pruneChainBreaks(pairDict)
    pruneNonePairs(pairDict)        #Remove uniques that may have resulted from removing residue sequences with chain breaks.
    logFile.close()
    return pairDict

def pruneNonePairs(pairDict):
    '''
    Remove all residue sequences that only occur in once in the given dictionary.
    
    Key argument:
     pairDict - dict
        Dictionary containing residue sequences.
    '''
    for key, val in pairDict.items():
        if len(pairDict[key]) < 2:
            del pairDict[key]

    
def pruneChainBreaks(pairDict):
    '''
    Calculate distances between all consecutive C-alpha atoms in all residue sequences in the given dictionary of pairs.
    Removes all residue sequences where the distance between two C-alpha atoms is greater than 4 angstrom.
    
    Key argument:
    pairDict - dict
        Dictionary containing residue sequences.
    '''
    for key, val in pairDict.items():
        for n, seq in val.items():
            chainBeaks = 0
            for idx in range(len(seq)-1):
                residueOne = seq[idx]
                residueTwo = seq[idx + 1]
                coordOne = residueOne["CA"].get_coord()
                coordTwo =  residueTwo["CA"].get_coord()
                normOne = numpy.linalg.norm(coordOne)
                normTwo = numpy.linalg.norm(coordTwo)
                distance = abs(normOne - normTwo)
                if distance > 4:
                    chainBeaks += 1
            if chainBeaks > 0:
                del pairDict[key][n]
    

def getRmsdValues(pairDict):
    '''
    Calculate Root Mean Square Deviation for sequence pairs give a pair-dictionary.
    Key arguments
    pairDict : dict
        Dictionary containing all residue sequences of a specified length that occur in two or more pdb files.
    '''
    RMSDList = []
    for key, val in pairDict.items():
        seqList = []
        for n, seq in val.items():
            seqList.append(seq)
        for xSeq, ySeq in itertools.combinations(seqList,2):
            pairLength = float(len(xSeq))
            xCoords = []
            yCoords = []
            for index in range(len(xSeq)):
                xCoords.append(xSeq[index]["CA"].get_coord())
                yCoords.append(ySeq[index]["CA"].get_coord())
            #x and y should be {3,pairLength} matrices
            x = numpy.mat(xCoords).transpose()
            y = numpy.mat(yCoords).transpose()
            #SVD:
            R = y * x.transpose()
            v, s, wt = numpy.linalg.svd(R)
            z = numpy.diag((1,1,-1))
            u = wt.transpose() * v.transpose()
            #Check for reflection:
            if numpy.linalg.det(u) == -1:
                u = wt.transpose() * z * v.transpose()
            
            #Transpose x and y again to correctly read the vectors.
            x = x.transpose()
            y = y.transpose()
            sum = 0
            for vectorIndex in range(len(x)):
                norm = numpy.linalg.norm(x[vectorIndex] - y[vectorIndex]*u)
                sum += norm**2
            RMSD = ((1/pairLength) * sum) ** 0.5
            RMSDList.append(RMSD)
    return RMSDList
    
    
if __name__ == '__main__':
    main()