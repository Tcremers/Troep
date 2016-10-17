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
    idDictTwo = handin6.fasta_names_to_dict(inFileNameTwo)
    
    print "File one unique ID's: " + str(getFileOneUniques(idListOne, idDictTwo))
    print "done"
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
def getFileOneUniques(idList, idDict):
    '''
    Given two lists, returns the number of uniques in list one.
    '''
    fileOneUniques = 0
    for idOne in idList:
        if idOne not in idDict:
            fileOneUniques += 1
            
    return fileOneUniques



if __name__ == '__main__':
    main()