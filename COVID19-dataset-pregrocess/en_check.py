# coding:utf-8

from enchant.checker import SpellChecker
#chkr = SpellChecker("en_US")
#chkr.set_text(data)
#for err in chkr :
    #print("ERROR", err.word)


import cld2
import json
import pandas as pd

with open('./1.json', 'rb') as f:
    data = json.load(f)

data = data['news_list']

en_data = []

for val in data:
    s = val.get('news_content')
    c = val.get('news_country')
    if s != '' and c != 'Russia':
        isReliable, textBytesFound, details = cld2.detect(s) 
        if details[0][0] == 'ENGLISH':
            en_data.append(val)

df  = pd.DataFrame([[0,0,0,0,0,0,0,0]])
df.columns = ['news_title','news_content','news_country','emotion','stance_against_china','about_china','topic','type']

count = 0

for val in en_data:
    a = val.get('news_title'); b = val.get('news_content'); c = val.get('news_country'); d = val.get('emotion')
    e = val.get('stance_against_china'); f = val.get('about_china'); g = val.get('topic'); h = val.get('type')
    a = a.replace('\n', ' ')
    b = b.replace('\n', ' ')
    c = c.replace('\n', ' ')
    d = d.replace('\n', ' ')
    e = e.replace('\n', ' ')
    g = g.replace('\n', ' ')
    h = h.replace('\n', ' ')
    df.loc[count] = [a, b, c, d, e, f, g, h]
    count += 1

df.to_csv('./1.csv', index=False)
print("Succeed!")


#isReliable, textBytesFound, details = cld2.detect(data)

