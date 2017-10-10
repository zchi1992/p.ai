import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
import re
import pattern
from pattern.en import conjugate
import xlrd


custom_stopwords = set((u"'s"))
all_stopwords = set(nltk.corpus.stopwords.words('english'))
all_stopwords.add("'s")

wnl = WordNetLemmatizer()

df = pd.read_csv("C:\\Users\\ChuyaoShen\\Desktop\\pianzi\\Pet\\Vetarycom\\cat_clean_data.csv")

dic_orig = ""
Symptoms_Key = list(df.Symptoms_Key.dropna())
for symptom in Symptoms_Key:
    dic_orig += " " + symptom.replace('/',' ')

dic_orig = re.sub('[^a-zA-Z0-9\n\.]', ' ', dic_orig)

dic_orig = nltk.word_tokenize(dic_orig)

dic_orig = [word for word in dic_orig if len(word) > 1]

dic_orig = [word for word in dic_orig if not unicode(word, 'utf-8').isnumeric()]

dic_orig = [word.lower() for word in dic_orig]

dic_orig = [word for word in dic_orig if word not in all_stopwords]

dic_orig = [wnl.lemmatize(word) for word in dic_orig]

dic_orig = [ conjugate(word) for word in dic_orig]

dic_orig = list(set(dic_orig))




dic_new = ""
Introduction = list(df.Introduction.dropna())
for sentence in Introduction:
    dic_new += " " + sentence

Symptoms_Detailed1 = list(df.Symptoms_Detailed1.dropna())
for sentence in Symptoms_Detailed1:
    dic_new += " " + sentence

Causes = list(df.Causes.dropna())
for sentence in Causes:
    dic_new += " " + sentence

Diagnosis = list(df.Diagnosis.dropna())
for sentence in Diagnosis:
    dic_new += " " + sentence

dic_new = dic_new.replace("\r"," ").replace("\n", " ")

dic_new = re.sub('[^a-zA-Z0-9\n\.]', ' ', dic_new)

dic_new = nltk.word_tokenize(dic_new)

dic_new = [word for word in dic_new if len(word) > 1]

dic_new = [word for word in dic_new if not unicode(word, 'utf-8').isnumeric()]

dic_new = [word.lower() for word in dic_new]

dic_new = [word for word in dic_new if word not in all_stopwords]

dic_new = [wnl.lemmatize(word) for word in dic_new]

dic_new = [ conjugate(word) for word in dic_new]

dic_new = list(set(dic_new))


dic = []
dic.extend(dic_orig)
dic.extend(dic_new)
dic = sorted(list(set(dic)))

dic = [word for word in dic if not (any(str.isdigit(c) for c in word.encode("ascii",'ignore')))]

dic = pd.DataFrame(dic, columns = ["word"])
dic.to_csv("C:\\Website\\P.AI\\dictionary.csv")


#############################################################
df = pd.read_csv("Z:\\P.AI\\Model\\cat_clean_data.csv")
df = df.fillna('')
data = pd.read_excel("Z:\\P.AI\\Model\\Training_Set.xlsx")
dic = pd.read_csv("Z:\\P.AI\\Model\\dictionary.csv")

for i in range(len(df.Disease)):
    print i
    Disease = df.Disease[i]
    string = df.Symptoms_Key[i] + " " + df.Introduction[i] + " " + df.Symptoms_Detailed1[i] + " " + df.Causes[i] + " " + df.Diagnosis[i]
    string = re.sub('[^a-zA-Z]', ' ', string)
    string = nltk.word_tokenize(string)
    string = [word.lower() for word in string]
    string = [wnl.lemmatize(word) for word in string]
    string = [conjugate(word) for word in string]
    string = list(set(string))
    string = [word for word in string if word is not None]
    string = [word.encode('ascii', 'ignore') for word in string]
    string = sorted(string)
    data[Disease][data.index.isin(string)] =1  

data.to_csv("C:\\Website\\P.AI\\data_1.csv")