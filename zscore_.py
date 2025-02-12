
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(0)
veri= np.random.normal(20,3,10000)
veriz= stats.zscore(veri)

sns.histplot(veriz)
plt.title("NORMAL DISTRIBUTION",c="g")
plt.xlabel("x ekseni",c="b")
plt.ylabel("FREKANS",c="r")
plt.axvline(x=np.mean(veriz)-1,linestyle="--",linewidth=3,c="r",label="Ortalama 1 Standart Sapma")
plt.axvline(x=np.mean(veriz)+1,linestyle="--",linewidth=3,c="r")
plt.axvline(x=np.mean(veriz)-2,linestyle="--",linewidth=3,c="black",label="Ortalama 2 Standart Sapma")
plt.axvline(x=np.mean(veriz)+2,linestyle="--",linewidth=3,c="black",)
plt.legend()
plt.show()

