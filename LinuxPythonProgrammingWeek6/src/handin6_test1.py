'''
Created on Oct 17, 2016

@author: Tycho
Linux and Python programming hand in week 6
'''
import handin6
import time


def main():
#     inFileNameOne = "C:\\Users\\Tycho\\Documents\\linux en python\\test1.fasta"
#     inFileNameTwo = "C:\\Users\\Tycho\\Documents\\linux en python\\test2.fasta"
    
    start_time = time.time()
    inFileNameOne = "C:\\Users\\Tycho\\Documents\\linux en python\\uniprot_sprot_2007.fasta"
    inFileNameTwo = "C:\\Users\\Tycho\\Documents\\linux en python\\uniprot_sprot_2015.fasta"
    
    idListOne = handin6.fasta_names_to_list(inFileNameOne)
    idListTwo = handin6.fasta_names_to_list(inFileNameTwo)
    
    print "File one unique ID's: " + str(getFileOneUniques(idListOne, idListTwo))
    print "done"
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
def getFileOneUniques(idListOne, idListTwo):
    '''
    Given two lists, returns the number of uniques in list one.
    '''
    fileOneUniques = len(idListOne)
    for idOne in idListOne:
        for idTwo in idListTwo:
            if idOne == idTwo:
                fileOneUniques -= 1
    return fileOneUniques


if __name__ == '__main__':
    main()