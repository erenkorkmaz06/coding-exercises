import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns
import statsmodels.api as sm
from scipy.stats import alpha
from  statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split,cross_val_score
import sklearn.metrics as mt
from sklearn.linear_model import LinearRegression, Ridge,Lasso, ElasticNet



data = pd.read_csv("C:/Users/erenk/Desktop/ev.csv")
veri = data.copy()
### veri.info() , veri.isnull().sum()

veri = veri.drop(columns="Address",axis=1)

###sns.pairplot(veri)
#plt.show()

###kor = veri.corr()
#sns.heatmap(kor,annot=True)
#plt.show()###

y = veri["Price"]
X = veri.drop(columns="Price",axis=1)

###sabit = sm.add_constant(X)
#vif = pd.DataFrame()
#vif["Değişkenler"] = X.columns
#vif["VİF"] = [variance_inflation_factor(sabit,i+1) for i in range(X.shape[1])]
#print(vif)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


def caprazdog(model):
    dogruluk = cross_val_score(model,X,y,cv=10)
    return dogruluk.mean()
def basarı(gercek,tahmin):
    rmse= mt.root_mean_squared_error(gercek,tahmin,)
    r2= mt.r2_score(gercek,tahmin)
    return [rmse,r2]

lin_model = LinearRegression()

lin_model.fit(X_train,y_train)
lin_tahmin = lin_model.predict(X_test)

ridge_model = Ridge(alpha=0.1)
ridge_model.fit(X_train,y_train)
rigde_tahmin = ridge_model.predict(X_test)

lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train,y_train)
lasso_tahmin = lasso_model.predict(X_test)

elas_model = ElasticNet(alpha=0.1)
elas_model.fit(X_train,y_train)
elas_tahmin = elas_model.predict(X_test)

sonuclar= [["Linear Model",basarı(y_test,lin_tahmin)[0],basarı(y_test,lin_tahmin)[1],caprazdog(lin_model)],
["Ridge Model",basarı(y_test,rigde_tahmin)[0],basarı(y_test,rigde_tahmin)[1],caprazdog(ridge_model)],
["Lasso Model",basarı(y_test,lasso_tahmin)[0],basarı(y_test,lasso_tahmin)[1],caprazdog(lasso_model)],
["Elasticnet Model",basarı(y_test,elas_tahmin)[0],basarı(y_test,elas_tahmin)[1],caprazdog(elas_model)]]

sonuclar = pd.DataFrame(sonuclar,columns=["Model","rmse","r2","Doğrulama"])

print(sonuclar)


