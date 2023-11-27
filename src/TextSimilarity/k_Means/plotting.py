import numpy as np
import matplotlib.pyplot as plt

def plot_clusters(data, labels, centroids):
    k = len(np.unique(labels))
    
    for i in range(k):
        plt.scatter(data[labels == i, 0], data[labels == i, 1], alpha=0.7, label=f'Data Cluster {i+1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering')
    plt.legend()
    plt.show()

