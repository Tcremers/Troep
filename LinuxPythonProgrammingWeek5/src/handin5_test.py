'''
Created on Oct 9, 2016

@author: Tycho

Linux and Python Programming hand in Week 5
'''
import sys
import handin5


def main():
    inFilePath = 'C:\Users\Tycho\Documents\linux en python\Ecoli.prot.fasta'
    print "Infile path:", inFilePath
    try:
        fastaDict = handin5.read_fasta(inFilePath)    
    except IOError:
        print sys.exc_info()[0]
        print sys.exc_info()[1]
    except:
        print "Something went wrong."
        print "Unexpected Error: " + str(sys.exc_info()[0])
        print sys.exc_info()[1]
    handin5.find_prot(fastaDict,"YHCN_ECOLI")
    handin5.find_prot(fastaDict,"SULA_ECOLI")
    handin5.find_prot(fastaDict,"BOOM_ECOLI")
    keyList = handin5.find_prot2(fastaDict, ".{3}_ECOLI")
    print "printing keys in keyList: "
    for key in keyList:
        print key
    
        
if __name__ == "__main__":
    main()