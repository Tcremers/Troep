'''
Created on Mar 22, 2017

    @author: Tycho
    '''
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
import math
import numpy as np


def main():
    print "hello world"
    fileName = "Chimpanzee_allele_freq.txt"
    with open(fileName,'r') as f:
        inFile = f.readlines()
    windows = getWindows(inFile, 10)
    
    #Calculate fsts data
    STfsts, SVfsts, TVfsts, positions = getFsts(windows)
    STavarage, SVavarage, TVavarage = getMeans(STfsts, SVfsts, TVfsts)
    STstd, SVstd, TVstd = getStds(STfsts, SVfsts, TVfsts)
    
    #Calculate pbs data
    pbsSs, pbsTs, pbsVs = calcPBS(STfsts, SVfsts, TVfsts)
    pbsSmean, pbsTmean, pbsVmean = getMeans(pbsSs, pbsTs, pbsVs)
    pbsSstd, pbsTstd, pbsVstd = getStds(pbsSs, pbsTs, pbsVs)
    getMaxPbs(pbsVs, positions, 100)
#     plotPerChromosome(pbsSs, positions, "PBS value: Schwein")
    plotPerChromosome(pbsTs, positions, "PBS value: Trogr")
#     plotPerChromosome(pbsVs, positions, "PBS value: Verus")
#     


#     STnormalized = normalizeData(STfsts, STavarage, STstd)
#     SVnormalized = normalizeData(SVfsts, SVavarage, SVstd)
#     TVnormalized = normalizeData(TVfsts, TVavarage, TVstd)
#     Snormalized, Tnormalized, Vnormalized = calcPBS(STnormalized, SVnormalized, TVnormalized)
#     pbsSnormalized = normalizeData(pbsSs, pbsSmean, pbsSstd)
#     pbsTnormalized = normalizeData(pbsTs, pbsTmean, pbsTstd)
#     pbsVnormalized = normalizeData(pbsVs, pbsVmean, pbsVstd)    
    print "ST: " + str(STavarage)
    print "SV: " + str(SVavarage)
    print "TV: " + str(TVavarage)
    
    print "S: " + str(pbsSmean)
    print "T: " + str(pbsTmean)
    print "V: " + str(pbsVmean)
    
    print "Done!"


def getMaxPbs(data, positions, n):
    '''
    Retrieve the n highest PVS values from the given data.
    
    data : list
        list of SNP pbs values
    positions : list
        list of SNP positions corresponding to the pbs values
    n : int
        number of pbs values to be retrieved.
    '''
    dataDict = {}
    maxPbs = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            dataDict [data[i][j]] = str(str(i+1)+"\t"+str(positions[i][j]))
    maxVals = sorted(dataDict.keys(), reverse = True)[:n]

    for val in maxVals:
        maxPbs[val] = dataDict[val]
        print str(val) +"\t" + dataDict[val]
    
    


def getMeans(first, second, third):
    #Don't actually have to be fsts values, pbs also allowed.
    '''
    Calculate the mean pdf or fsts value of the entire data set.
    
    first, second, third : lists
        lists of SNP pbs/fsts values
    '''
    print "Calculating means..."
    firstAvarage = []  #One
    secondAvarage = []  #Two
    thirdAvarage = []  #Three
    for i in range(len(first)):
        for j in range(len(first[i])):
            firstAvarage.append(first[i][j])
            secondAvarage.append(second[i][j])
            thirdAvarage.append(third[i][j])
    firstAvarage = np.mean(firstAvarage)
    secondAvarage = np.mean(secondAvarage)
    thirdAvarage = np.mean(thirdAvarage)
    return firstAvarage, secondAvarage, thirdAvarage
    
def getStds(first, second, third):
    '''
    Calculate the standard deviation of the pdf or fsts values of the entire data set.
    
    first, second, third : lists
        lists of SNP pbs/fsts values
    '''
    #Don't actually have to be fsts values, pbs also allowed.
    print "Calculating stds..."
    firstStd = []  #One
    secondStd = []  #Two
    thirdStd = []  #Three
    for i in range(len(first)):
        for j in range(len(first[i])):
            firstStd.append(first[i][j])
            secondStd.append(second[i][j])
            thirdStd.append(third[i][j])
    firstStd = np.std(firstStd)
    secondStd = np.std(secondStd)
    thirdStd = np.std(thirdStd)
    
    
    return firstStd, secondStd, thirdStd
    
    
    
    
def normalizeData(data, mean, sd):
    '''
    Normalize the given data set.
    
    data : list 
        list of SNP fst or pbs values.
    mean : float
        mean of the data set
    sd : float
        standard deviation of the given data set.
    '''
    
    #(X - mean )/ sd
    normalizedData = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            x = float((data[i][j] - mean)) / sd
            temp.append(x)
        normalizedData.append(temp)
    return normalizedData
    
def calcPBS(STfsts, SVfsts, TVfsts):
    '''
    Calculate the PBS values for the three given fsts data sets.
    
    STfsts : list
        fst values for Schwein compared to Trogr
    SVfsts : list
        fst values for Schwein compared to Verus
    TVfsts : list
        fst values for Trogr compared to Verus
    '''
    print "Calculating PBSs\n"
    pbsSs = []
    pbsTs = []
    pbsVs = []
    
    for i in range(len(STfsts)):
        pbsS = []
        pbsT = []
        pbsV = []
                
        for j in range(len(STfsts[i])):
            tST = math.log10(1-STfsts[i][j])*-1
            tSV = math.log10(1-SVfsts[i][j])*-1
            tTV = math.log10(1-TVfsts[i][j])*-1
            
            S = (tST + tSV - tTV) / 2
            T = (tST + tTV - tSV) / 2
            V = (tSV + tTV - tST) / 2
            
            pbsS.append(S)
            pbsT.append(T)
            pbsV.append(V)
        pbsSs.append(pbsS)
        pbsTs.append(pbsT)
        pbsVs.append(pbsV)
    return pbsSs, pbsTs, pbsVs

def plotPerChromosome(data, positions, title = ""):
    '''
    Plot the data in the data set in a "per chromosome" manhatten plot.
    
    data : list
        list of SNP pbs or fsts values
    positions : list
        list of SNP positions corresponding to the pbs/fst values
    title : str
        title of the plot
    '''
    colMap = get_cmap(22)
    ind = 0
    indsAll = []
    
    for i in range(len(data)):
        inds = []
        for j in range(len(data[i])):
            inds.append(ind)
            ind += 1
        indsAll.append(inds)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x_labels = []
    x_labels_pos = []
    
    for idx, chromosome in enumerate(data):
        print "\r{0}".format((float(idx)/len(data))*100)
        x = indsAll[idx]
        ax.scatter(x,chromosome,s = 5, color = colMap(int(idx)))
        x_labels.append("chr-" + str(idx))
        x_labels_pos.append(np.mean(indsAll[idx]))
    
    ax.set_xticks(x_labels_pos)
    ax.set_xticklabels(x_labels)
#     plt.ylim(0,0.1)
    plt.xlabel("Chromosomes...")
    plt.title(title)
    plt.show()
    
def plotAll(data, positions, title = ""):
    '''
    Plot the data against the SNP positions in a normal scatter plot.
    
    data : list
        list of SNP pbs or fsts values
    positions : list
        list of SNP positions corresponding to the pbs/fst values
    title : str
        title of the plot
    '''
    print "Plot PBSs"
    
    colMap = get_cmap(22)    
    for idx, chromosome in enumerate(data):
        print "\r{0}".format((float(idx)/len(data))*100)
        plt.scatter(positions[idx],chromosome,s = 5, color = colMap(int(idx)))
    plt.xlabel("Position in chromosome")
    plt.title(title)
    plt.show()

    
    
def get_cmap(N):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct 
    RGB color.
    Used to color the chromosome in the plot functions.
    
    N : int
        number of required indexes
    '''
    color_norm  = colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = cmx.ScalarMappable(norm=color_norm, cmap='hsv') 
    def map_index_to_rgb_color(index):
        return scalar_map.to_rgba(index)
    return map_index_to_rgb_color

    
def getWindows(inFile, s):
    '''
    Returns a list of all possible "windows" of SNPs of size s. Windows containing s consecutive SNPs.
    
    inFile : str
        Raw string of the entire infile seperated by line endings.
    s : int
        window size
    '''
    windows = []
    window = []
    for idx, line in enumerate(inFile):
        line = line[:-1]
        if line[0] != "#":
            if idx + s < len(inFile):
                if inFile[idx+s][0] == inFile[idx][0]:
                    window = inFile[idx:idx+s]
                    windows.append(window)
    print "Created " + str(len(windows)) + " windows."
    return windows
    
def getFsts(windows):
    '''
    Calculate the avarage fsts for every population combination for every window within a single chromosome
    and calculates the avarage position of every such window.
    
    windows : list 
        list of all SNP windows 
    '''
    STfstsTemp = []
    STfsts = []
    
    SVfstsTemp = []
    SVfsts = []
    
    TVfstsTemp = []
    TVfsts = []
    
    positionsTemp = []
    positions = []
    
    chromosomeCurrent = 1
    print "Calculating FSTs..."
    for window in windows:
        fst = 0
        STavarage = []
        SVavarage = []
        TVavarage = []
        positionAvarage = 0
        chromosome = int(window[0].split("\t")[0])
        for snp in window:
            snp = snp.split("\t")
            positionAvarage += int(snp[1])
            schweinFreq = snp[-3].split(",")[1]
            troglFreq = snp[-2].split(",")[1]
            verusFreq = snp[-1].split(",")[1]
            
            STavarage.append(calcFst(float(schweinFreq), float(troglFreq)))
            SVavarage.append((float(schweinFreq), float(verusFreq)))
            TVavarage.append(calcFst(float(troglFreq), float(verusFreq)))
        STavarage = np.mean(filter(lambda a: a != None, STavarage))
        SVavarage = np.mean(filter(lambda a: a != None, SVavarage))
        TVavarage = np.mean(filter(lambda a: a != None, TVavarage))
        
        positionAvarage = positionAvarage / len(window)
        
        #If a single avarage is nan, ignore the SNP.
        if math.isnan(STavarage) or math.isnan(SVavarage) or math.isnan(TVavarage):
            continue
        
        #If we're in the same chromosome, keeping adding values.
        if chromosomeCurrent == chromosome:
            STfstsTemp.append(STavarage)
            SVfstsTemp.append(SVavarage)
            TVfstsTemp.append(TVavarage)
            positionsTemp.append(positionAvarage)
        else:       
            #If the chromosome changes, add the temporary arrays to the main array as one chromosome an start with the new chromosome.
            chromosomeCurrent = chromosome
            STfsts.append(STfstsTemp)
            SVfsts.append(SVfstsTemp)
            TVfsts.append(TVfstsTemp)
            positions.append(positionsTemp)
            positionsTemp = []
            STfstsTemp = []
            SVfstsTemp = []
            TVfstsTemp = []
            STfstsTemp.append(STavarage)
            SVfstsTemp.append(SVavarage)
            TVfstsTemp.append(TVavarage)
            positionsTemp.append(positionAvarage)
    
    print "Done."
    #Final arrays our now of shape: [chromosome1[snp1, snp2, snp3....][chromosome2[snp1, snp2, snp3....]etc...]
    return STfsts, SVfsts, TVfsts, positions
    

def calcFst(fa1,fa2):
    '''
    Calculate the FST value between two allele frequency values.
    
    fa1 : float
        allele freq 1
    fa2 : float
        allele freq 2
    '''
    #If both frequencies are 1, fst value = 0
    if fa1 + fa2 == 2:
        return 0
    #if both frequencies are 0, ignore this fsts value.
    elif fa1 + fa2 == 0:
        return None
    
    #Take the absolute value of the allele frequencies so it doesn't matter 
    #which allele in the genotype you pick.
    if fa1 != 0.5:
        fa1 = abs(fa1 - 0.5)
    if fa2 != 0.5:
        fa2 = abs(fa2 - 0.5)
    
    #Calculate the actual FST value.
    hs = fa1*(1-fa1) + fa2 * (1-fa2)
    s = abs(fa1 - fa2)
    ht = hs + (s*0.5)
    fst = (ht - hs) / ht
    
    return fst

if __name__ == '__main__':
    main()