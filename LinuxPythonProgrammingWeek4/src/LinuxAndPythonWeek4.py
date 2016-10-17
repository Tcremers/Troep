'''
Created on Sep 28, 2016

@author: Tycho

Linux and Python Programming hand in Week 4
'''
#from __future__ import division

def main():
    inFileName = "C:\Users\Tycho\Documents\linux en python\experimental_results.txt"
    print "Opening inFile..."
    experimentalResults = openInFile(inFileName)
    
    print "Calculating averages..."
    averages = getAverages(experimentalResults)
    
    print "Writing avereges to outfile..."
    outfile = open("C:\\Users\\Tycho\\Documents\\linux en python\\results.txt","w")
    outfile.write(str(averages[0]) + " " + str(averages[1]))
    outfile.close()
    
    print "Inverting the experimentalResults list..."
    flippedExperimentalResults = flipList(experimentalResults)
    
    print "Calculating averages of flipped list..."
    averages = getAverages(flippedExperimentalResults)
    
    print "Converting flipped list into a dictionary..."
    experimentalResultsDict = {"column1":flippedExperimentalResults[0], "column2":flippedExperimentalResults[1]}
    
    print "Printing 26th value of \'column2\'..."
    print experimentalResultsDict["column2"][25]
       
    
#Opens the input file and reads the contents to a list of tuples.
def openInFile(fileName):
    experimentalResults = []
    
    with open(fileName,'r') as f:
        inFile = f.readlines()    
    for line in inFile:
        line = line.split(" ")
        if len(line) == 2:
            results = (float(line[0]),float(line[1]))
            experimentalResults.append(results)
    return experimentalResults

#Calculates the average of the columns in experimentalResults and adds these values to a list.
def getAverages(experimentalResults):
    averages = []
    
    if len(experimentalResults) > 2:
        columnSum = sum([result[0] for result in experimentalResults])
        columnAvarage = columnSum / len(experimentalResults)
        averages.append(columnAvarage)
        
        columnSum = sum([result[1] for result in experimentalResults])
        columnAvarage = columnSum / len(experimentalResults)
        averages.append(columnAvarage)
    else:
        columnAvarage = sum(experimentalResults[0]) / len(experimentalResults[0])
        averages.append(columnAvarage)
        columnAvarage = sum(experimentalResults[1]) / len(experimentalResults[1])
        averages.append(columnAvarage)
        
    for average in averages:
        print average
    return averages

#Inverts the experimentalResults list from a list of tuples into a list of 2 lists containing the experimental results.
def flipList(experimentalResults):
    flippedList = []
    columnOne = []
    columnTwo = []
    
    for results in experimentalResults:
        columnOne.append(results[0])
        columnTwo.append(results[1])
    flippedList.append(columnOne)
    flippedList.append(columnTwo)
    
    print "Printing 26th value of 2nd column..."
    print(flippedList[1][25])
    
    return flippedList
    
if __name__ == "__main__":
    main()