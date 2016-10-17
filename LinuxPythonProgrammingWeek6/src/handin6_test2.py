'''
Created on Oct 17, 2016

@author: Tycho
Linux and Python programming hand in week 6
'''
import handin6
import time


def main():
    inFileNameOne = "C:\\Users\\Tycho\\Documents\\linux en python\\test1.fasta"
    inFileNameTwo = "C:\\Users\\Tycho\\Documents\\linux en python\\test2.fasta"
    
    start_time = time.time()
#     inFileNameOne = "C:\\Users\\Tycho\\Documents\\linux en python\\uniprot_sprot_2007.fasta"
#     inFileNameTwo = "C:\\Users\\Tycho\\Documents\\linux en python\\uniprot_sprot_2015.fasta"
#     
    IdListOne = handin6.fasta_names_to_list(inFileNameOne)
    IdListTwo = handin6.fasta_names_to_list(inFileNameTwo)
    
    print "File one unique ID's: " + str(getFileOneUniques(IdListOne, sorted(IdListTwo)))
    print "done"
    print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
def getFileOneUniques(idListOne, idListTwo):
    '''
    Given two lists, returns the number of uniques in list one.
    '''
    fileOneUniques = 0
    for idOne in idListOne:
        if not binary_search(idListTwo, idOne):
            fileOneUniques += 1
            
        
    return fileOneUniques

def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False
if __name__ == '__main__':
    main()