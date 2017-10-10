import pandas as pd
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import re
import pattern
from pattern.en import conjugate
import xlrd
from numpy import genfromtxt


# WordExtractor function is used to convert the plain sentence to a feature list
# E.g.  "My cat has been fighting and got a cut ear that has been bleeding his o
#        ver grommed it and now has hair loss and bleeding slightly" 
#                         will be converted to ----> [3281,2004,2623,897,910,3784,3825,5122,8076]
# where each number is the unique mapping of a keyword
#
# The function contains two inputs:
#       (1) sentence: plain user's input
#       (2) word2number: a dictionary that maps keyword to a number, this can be read from parameter database
def WordExtractor(sentence, word2number):
    # define stop words
    all_stopwords = set(nltk.corpus.stopwords.words('english'))
    all_stopwords.add("'s")
    wnl = WordNetLemmatizer()
    # delete all non alphabet characters
    sentence = re.sub('[^a-zA-Z0-9\n\.]', ' ', sentence)
    # tokenize
    words = nltk.word_tokenize(sentence)
    # delete word with length equal to 1
    words = [word for word in words if len(word) > 1]
    # delete number
    words = [word for word in words if not unicode(word, 'utf-8').isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in all_stopwords]
    # lemmatize
    words = [wnl.lemmatize(word) for word in words]
    # convert to present tense
    words = [ conjugate(word) for word in words]
    words = list(set(words))
    features = [word2number[word] for word in words if word in word2number.keys()]
    return features



# This function calculate the probability of top 5 diseases based on feature list (output of WordExtractor)
# number2disease: a dictionary that maps a number to corresponding disease name, this can be read from parameter database
# embeddings is the parameter of the first layer, this can be read from database
# nce_weight and nce_bias are patameters of the second layer, this can be read from database
def DiseaseMapping(features, number2disease, embeddings, nce_weight, nce_bias):
    def softmax(x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)
    context = np.mean(embeddings[features], axis = 0)
    output = softmax(context.dot(nce_weight) + nce_bias)
    result = sorted(zip(output, range(len(output))),reverse = True)
    probability = [x[0] for x in result[:5]]
    probability = [x/sum(probability) * 100 for x in probability]
    disease = [number2disease[x[1]] for x in result[:5]]
    return(list(zip(disease, probability)))


# following is an example of implement above two functions
if __name__ == "__main__":

    ## load parameters. This can be down from database or local
    # read keywords dictionary
    dic = pd.read_csv("C:\\Website\\P.AI\\dictionary.csv")
    # read disease dictionary
    dic_d = pd.read_csv("C:\\Website\\P.AI\\dictionary_disease.csv")
    # read word2vec parameters
    embeddings = genfromtxt("C:\\Website\\P.AI\\embeddings.csv", delimiter = " ")
    nce_weight = genfromtxt("C:\\Website\\P.AI\\nce_weight.csv", delimiter = " ")
    nce_bias = genfromtxt("C:\\Website\\P.AI\\nce_bias.csv", delimiter = " ")

    # generate variable word2number from keywords dictionary 
    word2number = dic.set_index('word')['idx'].to_dict()
    # generate variable number2word
    number2word = dic.set_index('idx')['word'].to_dict()

    # generate variable disease2number from disease dictionary
    disease2number = dic_d.set_index('Disease')['idx'].to_dict()
    # generate variable number2disease
    number2disease = dic_d.set_index('idx')['Disease'].to_dict()
    
    
    while(True):
        sentence = raw_input("\nPlease Discribe the Symptons: ")
        #features = [3281,2004,2623,897,910,3784,3825,5122,8076]
        features = WordExtractor(sentence, word2number)
        output = DiseaseMapping(features, number2disease, embeddings, nce_weight, nce_bias)
        for i in range(5):
            print("%i: Disease: %s , Probability: %f percentage\n" % ((i+1, output[i][0], output[i][1])))