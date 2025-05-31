## [Unsupervised Learning]

[return to readme](../readme.md)

### Document Clustering
Through this technique documents are grouped into clusters based on their content similarity; the objective is to discover inherent structures without predefined categories or labels.
There are some method to do that. One popular is:<br>
    - <b><i>K-means clustering</i></b>: it is a unsupervised machine learning algorithm used for partitioning a dataset into 'k' distinct subgroups or clusters. The algorithm iteratively assigns data points to clusters based on their similarity to the cluster centroids and updates the centroids to minimize the total within-cluster variance. In order to show you how it works I've made a script that uses this algorithm from scratch.<br>
    - <b><i>Affinity Propagation</i></b>: Affinity Propagation is a clustering algorithm designed to identify representative points within a dataset. Unlike traditional clustering methods where the number of clusters needs to be specified beforehand, Affinity Propagation determines both the number of clusters and the exemplars simultaneously. Simply put, the algorithm iteratively exchanges messages between data points to find a set of exemplars that maximize a combination of similarity and preference values. The data points are then assigned to the nearest exemplar, forming clusters. To illustrate how it works, I've created a script utilizing this algorithm, and the results are visualized for clarity.

[Back to top](#)

[return to readme](../readme.md)