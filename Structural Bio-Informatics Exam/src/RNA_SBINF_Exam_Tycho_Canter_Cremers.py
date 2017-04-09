'''
Created on Jan 22, 2017

@author: Tycho Canter Cremers

Structural Bio-informatics Exam
RNA part
'''
import re

def main():
    #Question 1(b)
    epsFile = "sequence1_dp.eps"
    basePairData = readEpsFile(epsFile)
    probCount = countBasePairProbabilities(0.8, 1, basePairData)
    print "Pos 1 \t Pos 2 \t Prob"
    for basePair in basePairData:
        print basePair[0] + "\t" + basePair[1] + "\t"+ str(basePair[2]) + "\t"
    print "Number of base pairs with a base-pair probability higher than 80%: " + str(probCount) + "\n"
    
    #Question 2
    epsFile = "sequence2_dp.eps"
    basePairData = readEpsFile(epsFile)
    probCount = countBasePairProbabilities(0.8, 1, basePairData)
    print "Pos 1 \t Pos 2 \t Prob"
    for basePair in basePairData:
        print basePair[0] + "\t" + basePair[1] + "\t"+ str(basePair[2]) + "\t"
    print "Number of base pairs with a base-pair probability higher than 80%: " + str(probCount) + "\n"
            
    #Question 3-6
    dotBracketOne = "..(((((((....))))))).....(((((((((((.((..(((...)))..)).)))))))))))...."
    dotBracketTwo = "..(((((((....))))))).(((((((..(((((((.....)))))))......)))))))........"
    dotBracketConsensus = "..(((((((....))))))).((..((((((((((((((((((...)))))))..)))))))))))..))"
    
    print "Dot-bracket one: " + dotBracketOne
    print "Dot-bracket two: " + dotBracketTwo
    print "Dot-bracket Concensus: " + dotBracketConsensus
    
    
    basePairDistance, hammingDistance = compareDotBracket(dotBracketOne, dotBracketTwo)
    print "Dotbracket Sequence 1 vs Sequence 2:"
    print "Base-pair distance is: " + str(basePairDistance)
    print "Hamming distance is: " + str(hammingDistance)
    print ""
    
    basePairDistance, hammingDistance = compareDotBracket(dotBracketOne, dotBracketConsensus)
    print "Dotbracket Sequence 1 vs consensus:"
    print "Base-pair distance is: " + str(basePairDistance)
    print "Hamming distance is: " + str(hammingDistance)
    print ""
    
    basePairDistance, hammingDistance = compareDotBracket(dotBracketTwo, dotBracketConsensus)
    print "Dotbracket Sequence 2 vs consensus:"
    print "Base-pair distance is: " + str(basePairDistance)
    print "Hamming distance is: " + str(hammingDistance)



def readEpsFile(inFileName):
    '''
    Returns a list of base-pair probabilities and their positions sorted by their probabilities given a .eps dotplot file.
    Additionally prints the sequence associated to the .eps file.
    
    Key arguments:
    inFilename : str
        Filename or path to .eps dotplot file containing base pair positions and probabilities.
    '''
    print "Reading: " + inFileName
    with open(inFileName,'r') as f:
        inFile = f.readlines()
    
    basePairData = []
    for idx, line in enumerate(inFile):
        line = line.split(" ")
        if line[0] == "/sequence":      #Print Sequence
            print "Sequence: " + inFile[idx + 1][:-2]
            
        if line[-1] == "ubox\n" and line[0] != "%":     #Gather base-pairs
            basePairData.append((line[0],line[1], float(line[2]) ** 2))
            
    basePairData.sort(key=lambda tup: tup[2], reverse = True)
    return basePairData

def countBasePairProbabilities(min, max, basePairData):
    '''
    Returns a count of all base-pare probabilities where min > probability < max.
    If min or max are None defined they default to min = 0 and max = 1.
    
    Key arguments:
    min : int
        Minimum probability
    max : int
        Maximum probability
    basePairData : array
        Array or list of base-pair probabilities and their positions.
    '''
    probCount = 0
    if min == None:
        min = 0
    elif max == None:
        max = 1
        
    if min > 1 :
        min = float(min)/100
    elif max > 1:
        max = float(max)/100
        
    for basePair in basePairData:       #
        if basePair[2] >= min and basePair[2] <= max:
            probCount += 1
    return probCount

def compareDotBracket(dotBracketOne, dotBracketTwo):
    '''
    Returns the base-pair distance and hamming distance between two dot-bracket sequences.

    Key arguments:
    dotBracketOne : str
        first dot-bracket sequence
    dotBracketTwo : str
        second dot-bracket sequence of equal length to dotBracketOne
    '''
    if len(dotBracketOne) != len(dotBracketTwo):
        raise ValueError('Dot-bracket sequence length are not equal. Check your input.')
        
    pattern = re.compile("(?:\.*\(+)*\.*\)+\.*(?:\)+\.*)*")     #Regex pattern to retrieve subsequent open-close sequences of brackets.
    dotBracketOneList = pattern.findall(dotBracketOne)          #Contain these sequences in a list.
    dotBracketOneOpen, dotBracketOneClose = getOpenCloseList(dotBracketOneList)
    dotBracketOneClose = reverseClosed(dotBracketOneClose)      #Reverse closed bracket indexes to correctly pair them with the open bracket indexes.
    pairListOne = getPairs(dotBracketOneOpen, dotBracketOneClose)   #Generate pairs of the open-close bracket indexes.

    dotBracketTwoList = pattern.findall(dotBracketTwo)          #Do the same for the second sequence.
    dotBracketTwoOpen, dotBracketTwoClose = getOpenCloseList(dotBracketTwoList)
    dotBracketTwoClose = reverseClosed(dotBracketTwoClose)
    pairListTwo = getPairs(dotBracketTwoOpen, dotBracketTwoClose)
    
    basePairDistance = getBasePairDistance(pairListOne, pairListTwo)
    hammingDistance = getHammingDistance(dotBracketOne, dotBracketTwo)
    
    return basePairDistance, hammingDistance
     
    
def getOpenCloseList(dotBracketList):
    '''
    Returns two lists containing the indexes of the opening and closing brackets respectively, given a dotBracketList.
    
    Key arguments:
    dotBracketList - List/Array
        List containing strings of all subsequent open-close brackets sequences.
    '''
    dotBracketOpen = []
    dotBracketClose = []
    totalLength = 0
    for i in range(len(dotBracketList)):
        open = []
        close = []
        for j in range(len(dotBracketList[i])):
            if dotBracketList[i][j] == "(":
                if i-1 >= 0:                    #If working on a n-th subsequent sequence of open brackets, add the length of the past index for correct base-pair matching.
                    open.append(j+totalLength)
                else:
                    open.append(j)
            elif dotBracketList[i][j] == ")":
                if i-1 >= 0:                    #Same for closed brackets.
                    close.append(j+totalLength)
                else:
                    close.append(j)
        dotBracketOpen.append(open)
        dotBracketClose.append(close)
        totalLength += len(dotBracketList[i])
    return dotBracketOpen, dotBracketClose
      
        
def reverseClosed(dotBracketClose):
    '''
    Reverses all elements of a closed bracket list of indexes given a closed bracket array.
    
    Key arguments:
    dotBracketClose : array/List
        A list of indexes of the closed brackets of all subsequent close bracket sequences.
    ''' 
    for idx in range(len(dotBracketClose)):
        dotBracketClose[idx] = list(reversed(dotBracketClose[idx]))
    return dotBracketClose
            
    
def getPairs(dotBracketOpen, dotBracketClose):
    '''
    Generate a list of pairs for open and closed bracket indexes given a list of open bracket indexes and a list of closed ones.
    
    Key arguments:
    dotBracketOpen : array/List
        A list of indexes of the open brackets of all subsequent close bracket sequences.
    dotBracketClose : array/List
        A list of indexes of the closed brackets of all subsequent close bracket sequences.
    '''
    pairList = []
    for i in range(len(dotBracketOpen)):
        for j in range(len(dotBracketOpen[i])):
            pair = str(dotBracketOpen[i][j]) + "-" + str(dotBracketClose[i][j])
            pairList.append(pair)
    return pairList
    
def getBasePairDistance(pairListOne, pairListTwo):
    '''
    Caculate the base-pair distance given two lists of open-close bracket index pairs.
    
    Key arguments:
    pairListOne : array/List
        First list of open-close bracket index pairs
    pairListOne : array/List
        Second list of open-close bracket index pairs, to be compared to the first one. Not necessarily of equal length.
    '''
    basePairDistance = 0 
    for pair in range(len(pairListOne)):
        if pairListOne[pair] not in pairListTwo:
            basePairDistance += 1
    for pair in range(len(pairListTwo)):        
        if pairListTwo[pair] not in pairListOne:
            basePairDistance += 1
    return basePairDistance

def getHammingDistance(dotBracketOne, dotBracketTwo):
    '''
    Calculate the hamming distance given two dot-bracket sequences.
        Key arguments:
    dotBracketOne : str
        first dot-bracket sequence
    dotBracketTwo : str
        second dot-bracket sequence of equal length to dotBracketOne
    '''
    hammingDistance = 0
    for idx in range(len(dotBracketOne)):
        if dotBracketOne[idx] != dotBracketTwo[idx]:
            hammingDistance += 1
    return hammingDistance
        

if __name__ == '__main__':
    main()