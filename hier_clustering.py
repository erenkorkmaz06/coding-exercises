import pandas as pd
from scipy.cluster.hierarchy import linkage,dendrogram
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns

data = pd.read_csv("C:/Users/erenk/Desktop/iris.csv")
veri = data.copy()

X =  veri.drop(columns=["Id","Species"],axis=1)

hcsingle = linkage(X,method="single")
hccomplete = linkage(X,method="complete")
hcaverage = linkage(X,method="average")
hccentroid = linkage(X,method="centroid")
hcmedian = linkage(X,method="median")
hcward = linkage(X,method="ward")

#fig,axes = plt.subplots(2,3)
#dendrogram(hcsingle,ax=axes[0,0])
#axes[0,0].set_title("Single")
#dendrogram(hccomplete,ax=axes[0,1])
#axes[0,1].set_title("Complete")
#dendrogram(hcaverage,ax=axes[0,2])
#axes[0,2].set_title("Average")
#dendrogram(hccentroid,ax=axes[1,0])
#axes[1,0].set_title("Centroid")
#dendrogram(hcmedian,ax=axes[1,1])
#axes[1,1].set_title("Median")
#dendrogram(hcward,ax=axes[1,2])
#axes[1,2].set_title("Ward")
#plt.show()


model = AgglomerativeClustering(n_clusters=2,linkage="average")
tahmin = model.fit_predict(X)

labels = model.labels_
sns.scatterplot(data=X,x="SepalLengthCm",y="SepalWidthCm",hue=labels,palette="deep")
plt.show()




























