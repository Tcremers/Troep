'''
Created on Nov 2, 2016
Linux and python programming exam

@author: Tycho Canter Cremers
'''
import re

    
def read_speeches(inFilePath):
    """
    Given an inFile of clinton or trump speeches, returns a dictionary where key = speech title and value = the corresponding speech
    Parameters
    ----------
    inFilePath : str
        File path towards input file containing presidential candidate speeches.
    """
    speechTitle = re.compile(r'(?<=# )[^:]+:', re.MULTILINE)
    speech = re.compile(r'(?<=: )[^#]+', re.MULTILINE)
    speechDict = {}
    with open(inFilePath,'r') as f:
        inFile = f.readlines()
        
    fileIndex = 0
    for line in inFile:         #delete lines starting with "["
        if line.startswith("["):
            del inFile[fileIndex]
        fileIndex += 1
    
    inFile = ''.join(inFile)        #turn inFile into string
    inFile = inFile.replace("\n", " ")      #remove newlines and excessive white space
    inFile = inFile.replace("  ", " ")
    
    matchspeechTitle = re.findall(speechTitle, inFile)      #gather speeches
    matchspeech = re.findall(speech, inFile)

    speechIndex = 0
    for speechTitle in matchspeechTitle:        #Make dictionary from speeches    
        speechDict[speechTitle] = matchspeech[speechIndex]
        speechIndex += 1
        
        
    return speechDict
    
def merge_speeches(speechList):
    '''
    Given a list of strings, returns a complete string of all elements in given list.
    
    Parameters
    ----------
    speechList: string array
        Input list of string
    '''
    return " ".join(speechList)

def count_words(textString):
    '''
    Given a string, returns the number of words in said string. (A word is defined as any number of character separated by whitespace)
    
    Parameters
    ----------
    textString : str
        Input text
    '''
    return len(textString.split())

def count_sentences(textString):
    '''
    Given a string, returns the number of sentences in said string.
    
    Parameters
    ----------
    textString : str
        Input text
    '''
    return len(re.split("\.|\?|\!", textString)) - 1         #Subtract 1 because "re.split()" adds the (empty) remainder of the string after the last .?! to the last index.

def count_syllables(textString):
    '''
    Given a string, returns the number of syllables in the given string.
    
    Parameters
    ----------
    textString : str
        Input text
    '''
    pattern = re.compile(r"[aiouy]+e*|e(?!d\b|ly)[aiouye]?|[td]ed|le\b")
    matchSyllables = re.findall(pattern, textString.lower())
    
    return len(matchSyllables)

def calculate_flesch_score(textString):
    '''
    Given a text, calculates and returns the flesch score for given text.
    
    Parameters
    ----------
    textString : str
        Input text
    '''
    number_of_words = count_words(textString)
    number_of_sentences = count_sentences(textString)
    number_of_syllables =  count_syllables(textString)
    fleshScore = 206.835 - 1.015 * number_of_words/number_of_sentences - 84.6 * number_of_syllables/number_of_words
    
    return fleshScore

def plot_scores(scores, output_filename):
    """
    Plots score distributions

    Parameters
    ----------
    scores : dict object
        The values of this dictionary are lists of scores to be plotted. The keys of the dictionary
        will be used as labels for the plot.

    output_filename : str
        The name of the file used where the plot will be saved.
    
    """

    import matplotlib.pyplot as plt

    x_values = range(1, len(scores)+1)
    y_values = scores.values()

    # Create a box/violin plot
    plt.violinplot(y_values, x_values)    # <- Fill in this line

    # Add labels on x-axis
    plt.setp(plt.gca(), xticks=x_values, xticklabels=scores.keys())

    # Save figure
    plt.savefig(output_filename)
    
    
def calculate_ngram_frequencies(textString, nGramLength):
    '''
    Given a string of text, calculates all world pairs of length n.
    For instance the sentence "I love Python" would contain three word pairs of length n = 1 ("I", "love", "Python"),
    two word pairs of length n = 2 ("I love") and ("love Python"),
    and one word pair of length n = 3 ("I love Python")
    Returns dictionary containing key: word pair and value: occurrences of that specific word pair in the text
    
    Parameters
    ----------
    textString : str
        Input string containing text.
    nGramLength : int
        definition of word pair length (n)
    '''
    nGramDict = {}
    sentences = re.findall(r'[^\.\?!"]+', textString)
    nGramList = []
    for sentence in sentences:          #Iterate over all sentences, one by one.
        sentence = sentence.split()
        if len(sentence) >= nGramLength:
            index = 0
            nGram = []
            while index < len(sentence) - (nGramLength - 1):        #Add each nGram in a sentence to a list of Ngrams.        
                for i in range(nGramLength):
                    nGram.append(sentence[index + i])
                index +=1
                nGramList.append(" ".join(nGram))
                nGram = []
    
    for nGram in nGramList:         #Add Ngrams to a dictionary
        if nGram in nGramDict:
            nGramDict[nGram] += 1
        else:
            nGramDict[nGram] = 1
    
    return nGramDict
                
def get_second(x):
    """returns the second item of x"""
    return x[1]
