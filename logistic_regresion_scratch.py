import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

class LogisticRegression():
    def __init__(self,lr=0.001,n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self,X,y):
        n_samples,n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_predicitons = np.dot(X,self.weights) + self.bias
            predictions = sigmoid(linear_predicitons)

            dw = (1/n_samples)*np.dot(X.T,(predictions-y))*2
            db = (1/n_samples)*np.sum(predictions-y)*2

            self.weights -= self.lr*dw
            self.bias -= self.lr*db

    def predict(self,X):
        linear_predicitons = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(linear_predicitons)
        class_pred = [0 if y<=0.5 else 1 for y in y_pred]
        return class_pred

bc = datasets.load_breast_cancer()
X,y = bc.data , bc.target
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

def accuracy(y_pred,y_test):
    return np.sum(y_pred==y_test)/len(y_test)

acc = accuracy(y_pred,y_test)
print(acc)


