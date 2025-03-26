import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets

cmap = ListedColormap(["#FF0000","#00FF00","#0000FF"])


def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))



class KNN():
    def __init__(self,k=3):
        self.k = k

    def fit(self,X,y):
        self.X_train = X
        self.y_train = y

    def predict(self,X):
        predictions = [self._predict(x) for  x in X]
        return predictions

    def _predict(self,x):
        distances = [euclidean_distance(x,x_train) for x_train in self.X_train]

        k_indices = np.argsort(distances)[:self.k]
        k_nearest_label = [self.y_train[i] for i in  k_indices]

        most_common = Counter(k_nearest_label).most_common()
        return most_common[0][0]

iris = datasets.load_iris()
X,y = iris.data , iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.2,random_state=42)

plt.figure()
plt.scatter(X[:,2],X[:,3],c=y,cmap=cmap,edgecolors="k",s=20)
#plt.show()



model = KNN(k=5)
model.fit(X_train,y_train)
pred = model.predict(X_test)


acc = np.sum(pred == y_test)/len(y_test)

print(acc)
