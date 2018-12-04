import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as sm
from sklearn.cluster import KMeans
from sklearn import preprocessing ,datasets
from sklearn.mixture import GaussianMixture

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target,columns = ['Targets'])

colormap = np.array(['red', 'lime', 'black'])

plt.figure(figsize=(14,7))

#K Mean Algorithm
model = KMeans(n_clusters=3)
model.fit(X)
plt.subplot(1, 2, 2)
plt.title('K Mean Classification')
plt.scatter(X[2],X[3], c=colormap[model.labels_])

xsa = preprocessing.StandardScaler().fit_transform(X)

#EM Algorithm
y_cluster_gmm = GaussianMixture(n_components=3).fit(xsa).predict(xsa)
plt.subplot(1, 2, 1)
plt.title('GMM Classification')
plt.scatter(X[2], X[3], c=colormap[y_cluster_gmm])

print("confusion matrix ",sm.confusion_matrix(y,y_cluster_gmm))

print("Accuracy score " , sm.accuracy_score(y,y_cluster_gmm))

plt.show()
