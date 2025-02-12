import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("C:/Users/erenk/Desktop/diabetes.csv")
veri = data.copy()
y = veri["Outcome"]
X = veri.drop("Outcome",axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

modeller = []
modeller.append(("Log Reg",LogisticRegression(random_state=0)))
modeller.append(("KNN",KNeighborsClassifier()))
modeller.append(("SVC",SVC(random_state=0)))
modeller.append(("Bayes",GaussianNB()))
modeller.append(("Decision Tree",DecisionTreeClassifier(random_state=0)))

def model_kur(model):
    model.fit(X_train,y_train)
    tahmin = model.predict(X_test)
    acs = accuracy_score(y_test,tahmin)
    return round(acs*100,2)

model_names = []
model_skor = []
for model in modeller:
     model_skor.append(model_kur(model[1]))
     model_names.append(model[0])

result1 = pd.DataFrame(model_names,columns=["Model"])
result2 = pd.DataFrame(model_skor,columns=["Skor"])
result = result1.join(result2)
print(result)


