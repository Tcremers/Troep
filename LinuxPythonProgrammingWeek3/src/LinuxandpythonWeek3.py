'''
Created on Sep 26, 2016

@author: Tycho

Files and nested structures
Hand in week 3 Linux and Python Programming

'''

def main():
    
    fileName = 'C:\\Users\\Tycho\\Documents\\linux en python\\bashrc.txt'
    with open(fileName,'r') as f:
        inFile = f.readlines()
    print "printing character 2 of line 6: " + inFile[5][2]
    
    print "The file contains " + str(len(inFile)) + " lines."
    
    wordCount = 0
    for chars in inFile[4]:
        if chars == " ":
            wordCount += 1
    print "line 5 (- the #) contains " + str(wordCount) + " words."
    
    WriteToOutFIle('C:\\Users\\Tycho\\Documents\\linux en python\\junk.txt', inFile)

    
# Opens and closes specified file and reads the file into a list line by line. Also removes the newlines that are added by readlines()
def getInFile(filename):
    with open(filename,'r') as f:
        inFile = f.readlines()
    
    inFileList = []
    for line in inFile:
        inFileList.append(line.strip("\n"))
    return inFileList

#Opens the specified write-to file and writes away line 2 to 5.
def WriteToOutFIle(outFileName, inFile):
    outFile = open(outFileName, "w")
    print "Printing to outfile..."
    for line in inFile[1:4]:
        outFile.write(line + "\n")
    print "Done."
    outFile.close()
    return outFile


main()