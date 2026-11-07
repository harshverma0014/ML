import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

X =np.array([
    [2,4],
    [10,12],
    [3,20],
    [30,11],
    [25,10],
    [2,4],
    [5,9],
    [13,21],
    [25,31],
    [15,18]
])

model=KMeans(
    n_clusters=2,
)

model.fit(X)

labels=model.labels_

centroids = model.cluster_centers_

print("cluster labels")
print(labels)

print("\n centroids")
print(centroids)

plt.scatter(
    X[:,0],
    X[:,1],
    c = labels
)

plt.scatter(
    centroids[:,0],
    centroids[:,1],
    marker="X",
    s=200
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-MEANS CLUSTERING")

plt.show()