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

#取次
dic_orig = ""
Symptoms_Key = list(df.Symptoms_Key.dropna())
for symptom in Symptoms_Key:
    dic_orig += " " + symptom.replace('/',' ')
#只留下字母，把数字和字符变成空格
dic_orig = re.sub('[^a-zA-Z]', ' ', dic_orig)
#tokenize,变成单个单词
dic_orig = nltk.word_tokenize(dic_orig)
#去掉单个字母
dic_orig = [word for word in dic_orig if len(word) > 1]
#变为小写
dic_orig = [word.lower() for word in dic_orig]
#去掉stopwords： the, is, I, he, she.....
dic_orig = [word for word in dic_orig if word not in all_stopwords]
#lemmatize，把复数变单数
dic_orig = [wnl.lemmatize(word) for word in dic_orig]
#conjugate，把事态变为现在时
dic_orig = [ conjugate(word) for word in dic_orig]
#conjugate之后可能会出现none的值，去掉none
dic_orig = [word for word in dic_orig if word is not None]
#取unique的值
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

dic_new = [word.lower() for word in dic_new]

dic_new = [word for word in dic_new if word not in all_stopwords]

dic_new = [wnl.lemmatize(word) for word in dic_new]

dic_new = [conjugate(word) for word in dic_new]

dic_new = [word for word in dic_new if word is not None]

dic_new = list(set(dic_new))


dic = []
dic.extend(dic_orig)
dic.extend(dic_new)
dic = sorted(list(set(dic)))

dic = [word for word in dic if not (any(str.isdigit(c) for c in word.encode("ascii",'ignore')))]

dic = pd.DataFrame(dic, columns = ["word"])
dic.to_csv("C:\\Website\\P.AI\\dictionary.csv")
