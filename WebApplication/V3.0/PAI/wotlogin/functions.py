import pandas as pd
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import re
import pattern3
from pattern3.en import conjugate
import xlrd
from numpy import genfromtxt
from wotlogin.models import *
import random





def WordExtractor(sentence):

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
    words = [word for word in words if not str(word).isnumeric()]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in all_stopwords]
    # lemmatize
    words = [wnl.lemmatize(word) for word in words]
    # convert to present tense
    words = [ conjugate(word) for word in words]
    words = list(set(words))
    word2number = {s[1]:s[2] for s in list(Dic.objects.values_list())}
    features = [word2number[word] for word in words if word in word2number.keys()]
    return features

def DiseaseMapping(features):
    def softmax(x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)
    embeddings = np.array([row[0].split(",") for row in list(CatEmbeddings.objects.values_list("row"))], np.float16)
    nce_weight = np.array([row[0].split(",") for row in list(CatNce_weight.objects.values_list("row"))], np.float16)
    nce_bias = np.array([row[0].split(",") for row in list(CatNce_bias.objects.values_list("row"))], np.float16).reshape(-1)
    context = np.mean(embeddings[features], axis = 0)
    output = softmax(context.dot(np.transpose(nce_weight)) + nce_bias)
    #The disease index start from 1
    result = sorted(zip(output, range(1,len(output)+1)),reverse = True)[:5]
    result = [[pair[0]/sum([i[0] for i in result]) , pair[1]] for pair in result]
    return(result)



def CalculatePotentialInfo(output):
    potentialInfo = []
    for i in range(len(output)):
        potentialInfo.extend(CatDisease.objects.get(pk=output[i][1]).symptoms.split("/"))
    potentialInfo = list(set(potentialInfo))
    return potentialInfo

def GenerateShowForm(addedinfo, potentialinfo, outcome):
    showform = {"addedinfo": addedinfo, "potentialinfo": potentialinfo}
    output = []
    color_set = ["badge-primary", "badge-success", "badge-danger", "badge-warning", "badge-info", "badge-light", "badge-dark"]
    for i in range(len(outcome)):
        disease = CatDisease.objects.get(pk=outcome[i][1])
        symptom_set = disease.symptoms.split('/')
        output_elm = {"name": disease.disease, "probability": outcome[i][0]*100, "introduction": disease.introduction, "symptoms": [{"symptom": symptom_set[i], "color": color_set[i%7]} for i in range(len(symptom_set))], "diagnosis":disease.diagnosis, "cause":disease.causes, "treatment": disease.recovery}
        output.append(output_elm)
    showform["output"] = output
    return showform
