'''
Created on Oct 9, 2016

@author: Tycho

Linux and Python Programming hand in Week 5
'''
from itertools import groupby
import re

#This function accepts a fasta file and return a dict containing the headers and sequences in the file.
def read_fasta(inFastaFilePath):
    """
    Given a fasta file, returns dict containing headers and corresponding sequences.
    Keyword arguments:
    inFastaFilePath -- Input file of fasta format.
    """
    print "Executing read_fasta()..."
    print "Reading file..."
    inFile = open(inFastaFilePath)
    # ditch the boolean (x[0]) and just keep the header or sequence since we know they alternate.
    faiter = (x[1] for x in groupby(inFile, lambda line: line[0] == ">"))
    fastaDict = {}
    for header in faiter:
        # drop the ">"
        header = header.next()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.next())
        fastaDict[header] = seq
    inFile.close()
    print "Done."
    return fastaDict

#Returns protein sequence from the fasta-based dictionary based of key: "protein name".
def find_prot(fastaDict, proteinName):
    '''
    Searches dictionary for key and returns value
    Keyword arguments:
    fastaDict -- Protein sequence dictionary where key = "protein name" and value = "protein sequence".
    proteinName -- string containing protein name used as key.
    '''
    
    print "Searching for sequence of " + proteinName +"..."
    try:
        sequence = fastaDict[proteinName]
    except KeyError:
        print "Error. \nProtein: '" + proteinName + "' could not be found."
        return None
    print "Sequence: " + sequence
    return sequence

#Searches dictionary for all keys matching a regex pattern and returns all values.
def find_prot2(fastaDict, proteinNameAsRegex):
    '''
    Searches dictionary for all keys matching a regex pattern and returns all values.
    Keyword arguments:
    fastaDict -- Protein sequence dictionary
    proteinNameAsRegex -- Regular expression defined by the user.
    '''
    
    keyList = []
    print "Finding keys with pattern: '"+ proteinNameAsRegex +"'..."
    
    for key in fastaDict:
        if re.match(proteinNameAsRegex, key):
            keyList.append(key)
    print "Done."
    return keyList
            
    
    
    
    