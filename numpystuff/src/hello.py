'''
Created on Dec 9, 2016

@author: Tycho
'''
import numpy
from numpy.linalg.linalg import svd


def main():
    mOne = numpy.mat([[1,2,3],
                      [1,0,0],
                      [5,4,1]])
    
    print mOne.T
    print mOne.reshape((9,1))
    print numpy.zeros((3,4,5))
    
#     v, s, wt = svd(mOne)
#     
#     print v
#     print "\n"
#     print s
#     print "\n"
#     print wt









if __name__ == '__main__':
    main()