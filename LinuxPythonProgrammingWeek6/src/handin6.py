'''
Created on Oct 17, 2016

@author: Tycho
Linux and Python programming hand in week 6
'''

import re
    
def fasta_names_to_list(inFileName):
    '''
    Given a fasta file, returns a list of all IDs
    '''
    with open(inFileName,'r') as f:
        inFile = f.readlines()
    idList = []   
    for line in inFile:
        if line.startswith(">"):
            idList.append(fasta_label_to_id(line))
    
    return idList
def fasta_names_to_dict(inFileName):
    '''
    Given a fasta file, returns a dictionary containing all IDs as keys. Values as empty strings.
    '''
    with open(inFileName,'r') as f:
        inFile = f.readlines()
    idDict = {}
     
    for line in inFile:
        if line.startswith(">"):
            idDict[fasta_label_to_id(line)] = ""
    
    return idDict

def fasta_label_to_id(label):
    """Extract meaningful ID from fasta label"""
    pattern = re.compile(r'>\w+[ |(]+(\w+)[ |)]')
    match = pattern.match(label)
    return match.group(1)
