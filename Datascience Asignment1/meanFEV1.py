# data is the datamatrix of the smoking dataset, e.g. as obtained by data = numpy.loadtxt('smoking.txt')
# should return a tuple containing average FEV1 of smokers and nonsmokers 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
mpl.use('agg')


def main():
    inFileName = "smoking.txt"
    with open(inFileName,'r') as f:
        inFile = f.readlines()
    smoking, nonSmoking = meanFEV1(inFile)
    
    smokingCapacity, nonSmokingCapacity, smokerCapacityMean, nonSmokerCapacityMean, smokerAge, nonSmokerAge = getData(smoking, nonSmoking)
    getDotPlot(smokingCapacity, nonSmokingCapacity)
    
    tTestStatistics = scipy.stats.ttest_ind(smokingCapacity, nonSmokingCapacity)
    print "tTest statistic pvalue: "
    print tTestStatistics[1]
    
    getAgeFevCorrelationPlot(smokingCapacity, nonSmokingCapacity, smokerAge, nonSmokerAge)
    getHist(smokerAge, nonSmokerAge)
    
    print "Plots and hists saved in working directory."
    print "Done."
    
def meanFEV1(data):
    smoking = []
    nonSmoking = []
    
    for line in data:
        line = line.split("\t")
        if line[4] == "1":
            smoking.append(line)
        elif line[4] == "0":
            nonSmoking.append(line)
    return smoking, nonSmoking


def getData(smoking, nonSmoking):
    smokingCapacity = []
    nonSmokingCapacity = []
    smokerCapacityMean = 0
    nonSmokerCapacityMean = 0
    smokerAge = []
    nonSmokerAge = []

    for smoker in smoking:
        smokingCapacity.append(float(smoker[1]))
        smokerCapacityMean += float(smoker[1])
        smokerAge.append(float(smoker[0]))
        
    for nonSmoker in nonSmoking:
        nonSmokingCapacity.append(float(nonSmoker[1]))
        nonSmokerCapacityMean += float(nonSmoker[1])
        nonSmokerAge.append(float(nonSmoker[0]))
        
    smokerCapacityMean = smokerCapacityMean / float(len(smoking))
    nonSmokerCapacityMean = nonSmokerCapacityMean / float(len(nonSmoking))

    print "Mean lung capacity for smokers: "
    print smokerCapacityMean
    print "Mean lung capacity for non smokers: "
    print nonSmokerCapacityMean
    
    return smokingCapacity, nonSmokingCapacity, smokerCapacityMean, nonSmokerCapacityMean, smokerAge, nonSmokerAge
    
def getDotPlot(smokingCapacity, nonSmokingCapacity):
    ## combine these different collections into one list    
    plotData = [smokingCapacity, nonSmokingCapacity]
    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    ax = fig.add_subplot(111)
    # Create the boxplot
    ax.boxplot(plotData)
    #Add names and titles
    ax.set_title("Lung capacity smokers vs nonSmokers")
    randomDists = ['Smoker', 'NonSmoker']
    xtickNames = plt.setp(ax, xticklabels=np.repeat(randomDists, 1))
    plt.setp(xtickNames, rotation=35, fontsize=10)
    # Save the figure
    fig.savefig('smokerPlot.png', bbox_inches='tight')
    #plt.show()
    
def getAgeFevCorrelationPlot(smokingCapacity, nonSmokingCapacity, smokerAge, nonSmokerAge):
    FEV = smokingCapacity + nonSmokingCapacity
    age = smokerAge + nonSmokerAge
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Scatterplot FEV1 vs age")
    ax.set_xlabel("FEV1", fontsize = 12)
    ax.set_ylabel("age", fontsize = 12)
    plt.scatter(FEV, age)
    fig.savefig('scatterPlot.png', bbox_inches='tight')
    #plt.show()
    
    print "Correlation coeficient: "
    print scipy.stats.stats.pearsonr(FEV, age)[0]

def getHist(smokerAge, nonSmokerAge):
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Histogram of smoker age.")
    plt.hist(smokerAge, histtype='bar', rwidth=0.8)
    ax.set_xlabel("Age", fontsize = 12)
    ax.set_ylabel("Frequency", fontsize = 12)
    fig.savefig('smokerAgeHist.png', bbox_inches='tight')
    #plt.show()
    
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_title("Histogram of nonsmoker age.")
    plt.hist(nonSmokerAge, histtype='bar', rwidth=0.8)
    ax.set_xlabel("Age", fontsize = 12)
    ax.set_ylabel("Frequency", fontsize = 12)
    fig.savefig('nonsmokerAgeHist.png', bbox_inches='tight')
    #plt.show()

    
    
    

if __name__ == '__main__':
    main()
