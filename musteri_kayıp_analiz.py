import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from  lazypredict.Supervised  import LazyClassifier
from  sklearn.svm import SVC,LinearSVC
from  sklearn.linear_model import RidgeClassifier , LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv("C:/Users/erenk/Desktop/musteri_kayıp.csv")
veri = data.copy()
veri = veri.drop("customerID",axis=1)

#for i in veri:
#    print(i)
#    print(veri[i].dtypes)
#    print(veri[i].unique())

veri["SeniorCitizen"]= ["Yes" if i == 1 else "No" for i in veri["SeniorCitizen"]]
veri["MultipleLines"] = ["Yes" if i == "Yes" else "No" for i in veri["MultipleLines"]]
veri["InternetService"] = ["No" if i == "No" else "Yes" for i in veri["InternetService"]]
veri["OnlineSecurity"] = ["Yes" if i == "Yes" else "No" for i in veri["OnlineSecurity"]]
veri["OnlineBackup"] = ["Yes" if i == "Yes" else "No" for i in veri["OnlineBackup"]]
veri["DeviceProtection"] = ["Yes" if i == "Yes" else "No" for i in veri["DeviceProtection"]]
veri["TechSupport"] = ["Yes" if i == "Yes" else "No" for i in veri["TechSupport"]]
veri["StreamingTV"] = ["Yes" if i == "Yes" else "No" for i in veri["StreamingTV"]]
veri["StreamingMovies"] = ["Yes" if i == "Yes" else "No" for i in veri["StreamingMovies"]]
veri["TotalCharges"] = pd.to_numeric(veri["TotalCharges"],errors="coerce")

#for i in veri:
#    print(i)
#    print(veri[i].dtypes)
#    print(veri[i].unique())

#print(veri.isnull().sum())

#print(veri[veri["tenure"]==0])

veri = veri.dropna()

#print(veri.describe().T)
#plt.boxplot(veri["tenure"])
#plt.show()

#print(veri.select_dtypes(include="object").columns)

le = LabelEncoder()
variable = veri.select_dtypes(include="object").columns
veri.update(veri[variable].apply(le.fit_transform ))

y = veri["Churn"].astype(int)
X = veri.drop(columns="Churn",axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#lzc = LazyClassifier()
#models,  prediction = lzc.fit(X_train,X_test,y_train,y_test)
#ordered = models.sort_values(by="Accuracy",ascending=True)

#plt.barh(ordered.index,ordered["Accuracy"])
#plt.show()

models = ["LinearSVC", "SVC","Ridge","Logistic","RandomForest","LGBM","XGBM"]

classes = [LinearSVC(random_state=0,C=0.1,loss="squared_hinge",penalty="l1"),SVC(random_state=0,C=1,gamma=0.1,kernel="rbf"),RidgeClassifier(random_state=0,alpha=1),
           LogisticRegression(random_state=0,C=0.1,penalty="l2"),
           RandomForestClassifier(random_state=0,criterion="gini",max_depth=10,min_samples_leaf=7,n_estimators=2000),
           LGBMClassifier(random_state=0,learning_rate=0.001,max_depth=8,n_estimators=2000,subsample=0.6),
           XGBClassifier(learning_rate=0.0009,max_depth=8,n_estimators=2000,subsample=0.8)]


#params = {
#    models[0]:{"C":[0.1,1.10,100],"penalty":["l1","l2"],"loss":["hinge","squared_hinge"]},
#    models[1]:{"C":[0.1,1,10],"kernel":["rbf","linear"],"gamma":[0.001,0.01]},
#    models[2]:{"alpha":[0.1,1,10]},
#    models[3]:{"penalty":["l1","l2","elasticnet"],"C":[0.1,1,10]},
#    models[4]:{"n_estimators":[40,80,100],"criterion":["gini","entorpy"],"max_depth":[2,5,10],"min_samples_leaf":[2,4,8]},
#    models[5]:{"learning_rate":[0.001,0.01],"n_estimators":[1000,2000],"max_depth":[4,8,10],"subsample":[0.6,0.8]},
#    models[6]:{"learning_rate":[0.001,0.01],"n_estimators":[1000,2000],"max_depth":[4,8,10],"subsample":[0.6,0.8]}
#}

def set_model(model):
    model.fit(X_train,y_train)
    return model

def get_score(model2):
    pred= set_model(model2).predict(X_test)
    acs= accuracy_score(y_test,pred)
    return round(acs*100,2)

#for i,j in zip(models,classes):
#    print(i)
#    grid= GridSearchCV(set_model(j),params[i],cv=10,n_jobs=-1)
#    grid.fit(X_train,y_train)
#    print(grid.best_params_)


accuracy = []

for i in classes:
    accuracy.append(get_score(i))

e = list(zip(models,accuracy))
result = pd.DataFrame(e,columns=["Models","Accuracy"])

print(result.sort_values(by="Accuracy",ascending=False))

























