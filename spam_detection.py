import pandas as pd
import chardet
import matplotlib.pyplot as plot
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np
#with open("C:/Users/erenk/Desktop/spam.csv","rb") as x:
#    sonuc = chardet.detect(x.read())
#print(sonuc)


data = pd.read_csv("C:/Users/erenk/Desktop/spam.csv",encoding='Windows-1252')
veri = data.copy()
veri = veri.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4" ],axis=1)

veri = veri.rename(columns={"v1": "etiket","v2":"sms"})

#print(veri.groupby("etiket").count())
veri=veri.drop_duplicates()
#print(veri.describe())

veri["karakter sayısı"] = veri["sms"].apply(len)

#veri.hist(column="karakter sayısı",by= "etiket",bins=50)
#plot.show()

veri.etiket= [1 if kod == "spam" else 0 for kod in veri.etiket]

def harfler(cumle):
    yer = re.compile("[^a-zA-Z]")
    return re.sub(yer," ",cumle)

durdurma =stopwords.words("english")

spam = []
ham = []
com_sen = []

for i in range(len(veri["sms"].values)):
    x = veri["sms"].values[i]
    y = veri["etiket"].values[i]

    clean = []
    sen = harfler(x)
    sen=sen.lower()

    for word in sen.split():
        if word not in durdurma:
            clean.append(word)

        if y == 1:
            spam.append(sen)
        else:
            ham.append(sen)

    com_sen.append(" ".join(clean))

veri["new sms"]=com_sen

veri= veri.drop(columns=["sms","karakter sayısı"],axis=1)

cv = CountVectorizer()

x = cv.fit_transform(veri["new sms"]).toarray()

y = veri["etiket"]

X = x

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

for i in np.arange(0.0,1.1,0.1):
    model= MultinomialNB(alpha=i)
    model.fit(X_train,y_train)
    tahmin = model.predict(X_test)
    score = accuracy_score(y_test,tahmin)
    print("ALPHA {} değeri için Skor: {}".format(round(i,1),round(score*100,2)))













































