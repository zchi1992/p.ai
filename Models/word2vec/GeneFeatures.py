import pandas as pd
import numpy as np

dic = pd.read_csv("Z:\\P.AI\\Model\\dictionary.csv")
dic_d = pd.read_csv("Z:\\P.AI\\Model\\dictionary_disease.csv")
data = pd.read_csv("Z:\\P.AI\\Model\\data_1.csv", index_col = 0)


word2number = dic.set_index('word')['idx'].to_dict()
number2word = dic.set_index('idx')['word'].to_dict()

disease2number = dic_d.set_index('Disease')['idx'].to_dict()
number2disease = dic_d.set_index('idx')['Disease'].to_dict()



train_data = pd.DataFrame(np.zeros([data.sum().sum(),2]),columns = ["input", "output"])
columns = data.columns.values
rows = data.index.values
i = 0
for c in columns:
    print(c)
    temp = data[c][data[c]==1]
    for r in temp.index.values:
        train_data.input[i] = word2number[r]
        train_data.output[i] = disease2number[c]
        i += 1

train_data.to_csv("Z:\\P.AI\\Model\\features.csv")