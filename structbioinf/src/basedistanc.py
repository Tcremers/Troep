import re

def main():
    dotBracketOne = ".....(((((.(((..(((((((((....)))))))))..)))))))).."
    dotBracketTwo = "......(.((((((..(((((((((....)))))))))..)))))).).."
    
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
    print basePairDistance
    return basePairDistance

def getHammingDistance(dotBracketOne, dotBracketTwo):
    hammingDistance = 0
    for idx in range(len(dotBracketOne)):
        if dotBracketOne[idx] != dotBracketTwo[idx]:
            hammingDistance += 1
    return hammingDistance

if __name__ == '__main__':
    main()