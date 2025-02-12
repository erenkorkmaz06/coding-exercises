import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import  StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

data = pd.read_csv("C:/Users/erenk/Desktop/diabetes.csv")
veri = data.copy()
y = veri["Outcome"]
X = veri.drop("Outcome",axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model= RandomForestClassifier(random_state=0)
model.fit(X_train,y_train)
tahmin= model.predict(X_test)


#params = {"criterion" : ["gini", "entropy", "log_loss"],
#"max_depth": [2,5,10,15,20,25],"min_samples_split":[2,3,4,5,6,7,8,9,10],"min_samples_leaf":[1,2,3,4,5,6,7,8,9],"n_estimators":[10,20,40,60,80,100,200,300,400]}

#grid = GridSearchCV(model,params,cv=10,n_jobs=-1)

#grid.fit(X_train,y_train)
#print(grid.best_params_)
model_tuned = RandomForestClassifier(random_state=0,criterion = "entropy",max_depth= 10,min_samples_split=9,n_estimators=60,min_samples_leaf=4)
model_tuned.fit(X_train,y_train)
tuned_tahmin = model_tuned.predict(X_test)

acs1 = accuracy_score(y_test,tahmin)
acs2 = accuracy_score(y_test,tuned_tahmin)

print((acs1,acs2))

#plot_tree(model_tuned[34],filled=True,fontsize=10)
#plt.show()