'''
Created on Oct 11, 2016

@author: Tycho
'''
from Bio import SeqIO
import re

def main():
    inFilePath = "C:\Users\Tycho\Documents\linux en python\EcoliGenome.fasta"
    sequence = readInFile(inFilePath)
    print "Does this work?"
    orfs(sequence)
        
    
    
def readInFile(inFilePath):
    inFile = open(inFilePath)
    seq = ""
    reverseComplement = ""
    for record in SeqIO.parse(inFile, "fasta"):
        sequence = record.seq
    return sequence


def orfs(sequence):
    pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
    allORFS = pattern.findall(str(sequence)) + pattern.findall(str(sequence.reverse_complement()))
    count = 0
    goodORFS = []
    for ORF in allORFS:
        if len(ORF) > 299:
            goodORFS.append(ORF)
    return goodORFS
    
if __name__ == '__main__':
    main()