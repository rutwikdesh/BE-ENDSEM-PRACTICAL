import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans

df = pd.read_csv('dataset.csv')

X = np.array(df)

c_x = np.array([0.1,0.3])
c_y = np.array([0.6,0.2])

centroids = np.array(list(zip(c_x,c_y)))
print(centroids)

model = KMeans()
model.fit(X, centroids)

plt.figure()
plt.scatter(X[:,0],X[:,1],alpha=0.3)
plt.show()

plt.figure()
plt.scatter(X[:,0],X[:,1],alpha=0.3)
plt.scatter(c_x,c_y, marker='o', c='black', s=150)
plt.show()