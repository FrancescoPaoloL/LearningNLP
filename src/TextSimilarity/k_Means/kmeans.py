import numpy as np

def k_means_clustering(data, k, max_iterations=100):
    # Step 1: Randomly initialize centroids
    centroids = data[np.random.choice(len(data), k, replace=False)]
    
    for _ in range(max_iterations):
        # Step 2: Assign data points to the nearest centroid
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        
        # Step 3: Update centroids
        for i in range(k):
            centroids[i] = np.mean(data[labels == i], axis=0)
    
    return labels, centroids

