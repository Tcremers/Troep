'''
Created on Nov 2, 2016
Linux and python programming exam

@author: Tycho Canter Cremers
'''
import exam

def main():
    clintonInFilePath = "C:\\Users\\Tycho\\Documents\\linux en python\\Exam\\clinton_speeches.txt"
    trumpInFilePath = "C:\\Users\\Tycho\\Documents\\linux en python\\Exam\\trump_speeches.txt"
    clinton_speeches_dict = exam.read_speeches(clintonInFilePath)
    trump_speeches_dict = exam.read_speeches(trumpInFilePath)
    
    print "Number of Clinton speeches: " + str(len(clinton_speeches_dict))
    print "Number of Trump speeches: " + str(len(trump_speeches_dict))
    
    print "\n"
    clinton_speeches_all = exam.merge_speeches(clinton_speeches_dict.values())
    trump_speeches_all = exam.merge_speeches(trump_speeches_dict.values())
    
    print "Length of clinton_speeches_all: " + str(len(clinton_speeches_all))
    print "Length of trump_speeches_all: " + str(len(trump_speeches_all))
    
    print "\n"
    
    print "Number of words in clinton_speeches_all: " + str(exam.count_words(clinton_speeches_all)) 
    print "Number of words in trump_speeches_all: " + str(exam.count_words(trump_speeches_all))
    
    print "\n"
    
    print "Number of sentences in trump_speeches_all: " + str(exam.count_sentences(trump_speeches_all))
    
    print "\n"
    
    print "Number of syllables in \"I eat apples\": " + str(exam.count_syllables("I eat apples"))
    
    print "\n"
    
    trump_scores = []
    clinton_scores = []
    for speech in trump_speeches_dict.values():
        trump_scores.append(exam.calculate_flesch_score(speech))
    for speech in clinton_speeches_dict.values():
        clinton_scores.append(exam.calculate_flesch_score(speech))
        
    print "Trump scores: "
    print trump_scores
    print "\n"
    print "Clinton scores: "
    print clinton_scores
    scoresDict = {"Trump flesch scores" : trump_scores , "Clinton flesch scores" : clinton_scores}
    
    print "\n"
    print "Plotting flesch scores..."
    exam.plot_scores(scoresDict, "flesch score plot")
    print "Done"
    
    print "\n"
    print "Calculate nGram dictionaries..."
    clinton_6gram_dict = exam.calculate_ngram_frequencies(clinton_speeches_all, 6)
    trump_6gram_dict = exam.calculate_ngram_frequencies(trump_speeches_all, 6)
    print "Done."
    
    clinton_6gram_dict_sorted = sorted(clinton_6gram_dict.items(), reverse = True, key=exam.get_second)
    trump_6gram_dict_sorted = sorted(trump_6gram_dict.items(), reverse = True, key=exam.get_second)
    
    print "\n"
    print "10 most frequent Clinton 6-grams: "
    for i in range(10):
        print clinton_6gram_dict_sorted[i]
        
    print "\n"
    print "10 most frequent Trump 6-grams: "
    for i in range(10):
        print trump_6gram_dict_sorted[i]
    
    
    
if __name__ == '__main__':
    main()