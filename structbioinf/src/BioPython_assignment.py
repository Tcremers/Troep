'''
Created on Jan 13, 2017

@author: Tycho

BioPDB assignment for Structural Bio-Informatics
'''

import Bio.PDB as pdb


def main():
    print "Parsing PDB file..."
    parser = pdb.PDBParser()
    structure = parser.get_structure('PHA-L', '2ptc.pdb')
    print "Done.\n"
    chain = structure[0]["E"]
    residue = chain[20]
    atom = residue["CA"]
    print atom.get_coord()
#
#     print "Coordinates of C-alpha atom of residue " + str(residue.get_id()[1]) + ", chain "  + str(chain.get_id()) + ": "
#     print atom.get_coord()
#     
#     print "Geometric central coordinate of residue " + str(residue.get_id()[1]) + ", chain "  + str(chain.get_id()) + ": " 
#     print getCentroidCoord(residue)
#     
#     print "\n"
#     chain = structure[0]["I"]
#     residue = chain[13]
#     atom = residue["CA"]
#     
#     print "Coordinates of C-alpha atom of residue " + str(residue.get_id()[1]) + ", chain "  + str(chain.get_id()) + ": "
#     print atom.get_coord()
#     
#     print "Geometric central coordinate of residue " + str(residue.get_id()[1]) + ", chain "  + str(chain.get_id()) + ": " 
#     print getCentroidCoord(residue)
    

def getCentroidCoord(residue):
    '''Calculate the geometric center of a residue given a PDB residue object'''
    coordsX = 0
    coordsY = 0
    coordsZ = 0
    for atoms in residue:
        coordsX += atoms.get_coord()[0]
        coordsY += atoms.get_coord()[1]
        coordsZ += atoms.get_coord()[2]
    
    coordsX = coordsX/len(residue)
    coordsY = coordsY/len(residue)
    coordsZ = coordsZ/len(residue)
    
    coordCentroid = [coordsX,coordsY,coordsZ]
    
    return coordCentroid
        
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()