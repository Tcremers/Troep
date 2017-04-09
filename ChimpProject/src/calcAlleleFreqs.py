'''
Created on Mar 21, 2017

@author: Tycho
'''

def main():
    #Input: A .vcf file
    fileName = "C:\\Users\\Tycho\\Documents\\Chimp project\\SNP_v37_version3.vcf"
#     fileName = "C:\Users\Tycho\Documents\Chimp project\\TestVcfData.txt"
    with open(fileName,'r') as f:
        inFile = f.readlines()
    outFile = open("Chimpanzee_allele_freq.txt", "w")
    outFile.write("#CHROM\tPOS\tID\tREF\tALT\tSchwein\trogl\tverus\n")
    
    print "Calculating SNP allele frequencies..."    
    total = []
    #Iterate over the lines in the file.
    for idx, line in enumerate(inFile):
        #If the line contains and SNP...
        if line[0:2] != "##" and line[0:2] != "#C":
            split = line.split("\t")
            snp = split[0:5]
            if len(split[4]) == 1:
                #Iterate over Schwein = [0:11] length = 11
                schweins = split[9:-2][0:11]
                schweinAlleleFreq = getAlleleFreq(schweins)
                #Iterate over Trogl = [11:22] length = 12
                trogls = split[9:-2][11:23]
                troglAlleleFreq = getAlleleFreq(trogls)
                #Iterate over Verus = [22:] length = 6
                veruss = split[9:-2][23:]
                verusAlleleFreq = getAlleleFreq(veruss)
                
                #snp = last three are schweins, trogl, verus
                snp.append(','.join(str(e) for e in schweinAlleleFreq))
                snp.append(','.join(str(e) for e in troglAlleleFreq))
                snp.append(','.join(str(e) for e in verusAlleleFreq))


                outFile.write("\t".join(snp))
                outFile.write("\n")
                total.append(snp)
                
    print "Done."
    print "Processed SNP count: " + str(len(total))


def getAlleleFreq(population, keepUnknown = False):
    '''
    Calculate the allele frequencies per SNP for each sub population.
    
    population : str
        One SNP(line) from the VCF file
    '''
    alleleFreq = [0,0]
    n = len(population)
    for individual in population:
        genoType = individual.split(":")[0].split("/")
        if genoType[0] != ".":
            for allele in genoType:
                if allele == "0":
                    alleleFreq[0] += 1
                elif allele == "1":
                    alleleFreq[1] += 1
        else:
            if keepUnknown == False:
                n -= 1
            else:
                n = n
            
    alleleFreq[0] = float(alleleFreq[0]) / (n * 2)
    alleleFreq[1] = float(alleleFreq[1]) / (n * 2)
    return alleleFreq
    
if __name__ == '__main__':
    main()
