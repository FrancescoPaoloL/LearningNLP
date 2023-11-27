import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from sklearn.datasets import make_blobs
from itertools import cycle

def run_affinity_propagation():
    # Generate sample data
    centers = [[1, 1], [-1, -1], [1, -1], [-1, -1]]
    X, labels_true = make_blobs(n_samples=400, centers=centers, cluster_std=0.5, random_state=0)

    # Compute Affinity Propagation
    af = AffinityPropagation(preference=-50, random_state=0).fit(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)

    # Plot result
    plt.close('all')
    plt.figure(1)
    plt.clf()

    # it cycles through the characters 'b', 'g', 'r', 'c', 'm', 'y', 'k'
    # representing the colors blue, green, red, cyan, magenta, yellow, and black, respectively
    # we do that to assign different colors to different clusters when plotting the data points
    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')

    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)

        for x in X[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()

