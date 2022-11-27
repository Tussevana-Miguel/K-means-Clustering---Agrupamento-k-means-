@author: tussevana Miguel
"""


import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    random_state=42
)

#n_samples is the total number of samples to generate.
#centers is the number of centers to generate.
#cluster_std is the standard deviation.

#make_blobs() returns a tuple of two values:

#1 two-dimensional NumPy array with the x- and y-values for each of the samples
#2 one-dimensional NumPy array containing the cluster labels for each sample


print(features[:5])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(scaled_features[:7])
plt.scatter(scaled_features[:,0], scaled_features[:,1])
#Plot an histogram to analize the distribuition

plt.hist(scaled_features, bins=None)
plt.show()

kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
)

#init controls the initialization technique. The standard version of the 
   #k-means algorithm is implemented by setting init to "random". Setting this 
   #"k-means++" employs an advanced trick to speed up convergence, which you’ll use later.

#n_clusters sets k for the clustering step. This is the most important parameter for k-means.

#n_init sets the number of initializations to perform. This is important because two runs can 
    #converge on different cluster assignments. The default behavior for the scikit-learn algorithm 
    #is to perform ten k-means runs and return the results of the one with the lowest SSE.

#max_iter sets the number of maximum iterations for each initialization of the k-means algorithm.


kmeans.fit(scaled_features)

# The lowest SSE value
kmeans.inertia_

# Final locations of the centroid
kmeans.cluster_centers_

# The number of iterations required to converge
kmeans.n_iter_

#what point was related to what custer
kmeans.labels_[:5]

#Choosing the Appropriate Number of Clusters
#1 The elbow method
#2 The silhouette coefficient


#To perform the elbow method, run several k-means, increment k with each iteration, and record the SSE:
kmeans_kwargs = {
    "init": "random",
    "n_init": 10,
    "max_iter": 300,
    "random_state": 42,
}

# A list holds the SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)
    
#When you plot SSE as a function of the number of clusters, notice that SSE continues to decrease as you 
#increase k. As more centroids are added, the distance from each point to its closest centroid will 
#decrease.
    

# plot of SSE to identify the elbow
plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

#If you’re having trouble choosing the elbow point of the curve, then you could use a Python package, 
#kneed, to identify the elbow point programmatically:

kl = KneeLocator(
    range(1, 11), sse, curve="convex", direction="decreasing"
)

kl.elbow

#using the elbow method we have come to a conclusion that the suitable number of clusters is 3

#The silhouette coefficient is a measure of cluster cohesion and separation. It quantifies how well 
#a data point fits into its assigned cluster based on two factors:

#1 How close the data point is to other points in the cluster
#2 How far away the data point is from points in other clusters



#Silhouette coefficient values range between -1 and 1. Larger numbers indicate that samples are closer 
#to their clusters than they are to other clusters.


#Loop through values of k again. This time, instead of computing SSE, compute the silhouette coefficient:

# A list holds the silhouette coefficients for each k
silhouette_coefficients = []

# Notice you start at 2 clusters for silhouette coefficient
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)
    
#Plotting the average silhouette scores for each k shows that the best choice for k is 3 since it has 
#the maximum score:

plt.style.use("fivethirtyeight")
plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.show()

#Once all methods converge to 3 clusters lets go ahead and finish itp
kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
)

kmeans.fit(scaled_features)
y_km = kmeans.fit_predict(scaled_features)
print(y_km)

plt.scatter(scaled_features[y_km==2,0], scaled_features[y_km==2,1], s=50, color='blue')

plt.scatter(scaled_features[y_km==0,0], scaled_features[y_km==0,1], s=50, color='red')
plt.scatter(scaled_features[y_km==1,0], scaled_features[y_km==1,1], s=50, color='green')
plt.scatter(kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1], marker = "*", s=250, color='black')
plt.scatter(kmeans.cluster_centers_[1][0], kmeans.cluster_centers_[1][1], marker = "*", s=250, color='black')
plt.scatter(kmeans.cluster_centers_[2][0], kmeans.cluster_centers_[2][1], marker = "*", s=250, color='black')
plt.show()
