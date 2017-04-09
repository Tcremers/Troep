# import numpy
# 
# def idFunc(something):
#     print id(something)
#     del something["DERP"]
# 
# aminoAcidDict = {'CYS': [], 'ARG' : []}
# aminoAcidDict["CYS"].append(["hello"])
# aminoAcidDict["CYS"].append(["world"])
# aminoAcidDict["ARG"].append(["bar"])
# 
# aminoAcidDict["DERP"] = "waaahhh"
# 
# aminoAcidDict["DERP"] = "kkkuuuuut"
# 
# 
# m = numpy.mat([[1,2,3,4,5],[3,4,5,6,7],[5,6,7,8,9],[7,8,9,10,11],[8,9,10,11,12]])
# n = numpy.mat([(1,2),(3,4),(5,6)])
# o = n.transpose()
# 
# print n
# print o
# 
# print numpy.linalg.norm(n)
# print numpy.linalg.norm(o)


# test = ["1","2","3","4","5"]
# 
# test = test[1:5]
# test.append("6")
# print test

def getRandomPdbEntries():
    '''
    SeqType is either "prot" or "prot-nuc" or "nuc"
    '''
    from random import randint
    getIdsFile = open("cmpd_res.idx.txt", "r")
    isProtfile = open("pdb_entry_type.txt", "r")
    
    pdbIds = []
    prots = {}
    confirmedProts = []
    myProts = []
    lineCount = 0
    for line in getIdsFile:
        lineCount += 1
        if lineCount == 10:
            lineCount = 0
            line = line.split(";")
            pdbIds.append(line[0][0:len(line[0]) - 1].lower())
    for line in isProtfile:
        line = line.split("\t")
        if line[1] == "prot":
            prots[line[0]] = "something"
    #print prots
    for id in pdbIds:
        if id in prots:
            confirmedProts.append(id)
    
    randomnums = set()
    while len(randomnums) < 200:
        randomnums.add(randint(0,len(confirmedProts)))
    for randint in randomnums:
        myProts.append(confirmedProts[randint])
    
    
    print len(myProts[0:200])
        
getRandomPdbEntries()



