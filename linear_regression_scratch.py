import  numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

class LinearRegresiion:

    def __init__(self,lr=0.01,n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self,X,y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        for i in range(n_samples):
            y_pred = np.dot(X,self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T,(y_pred-y)) * 2
            db = (1/n_samples) * np.sum(y_pred-y) * 2

            self.weights -= self.lr * dw
            self.bias -= self.lr * db


    def predict(self,X):
        y_pred = np.dot(X, self.weights) + self.bias
        return  y_pred



X,y = datasets.make_regression(n_samples=1000,n_features=1,noise=20,random_state=0)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.2,random_state=123)

fig = plt.figure(figsize=(8,6))
plt.scatter(X[:,0],y,color="b",marker="o",s=30)

model = LinearRegresiion()
model.fit(X_train,y_train)
pred = model.predict(X_test)

def mse(y_test,predictions):
    return np.mean((y_test-predictions)**2)

mse = mse(y_test,pred)
print(mse)

y_pred_line = model.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train,y_train,color=cmap(0.9),s=10)
m2 = plt.scatter(X_test,y_test,color=cmap(0.5),s=10)
plt.plot(X,y_pred_line,color="black",linewidth=2,label="prediction")
plt.show()