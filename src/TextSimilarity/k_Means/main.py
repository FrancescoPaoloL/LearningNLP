import numpy as np
from kmeans import k_means_clustering
from plotting import plot_clusters

# Generate some random 2D data for demonstration
np.random.seed(42)
data = np.concatenate([np.random.normal(loc=(0, 0), scale=1, size=(50, 2)),
                       np.random.normal(loc=(5, 5), scale=1, size=(50, 2)),
                       np.random.normal(loc=(10, 0), scale=1, size=(50, 2))])

# Set the number of clusters
k = 3

# Apply k-means clustering
labels, centroids = k_means_clustering(data, k)

# Plot the clusters
plot_clusters(data, labels, centroids)

