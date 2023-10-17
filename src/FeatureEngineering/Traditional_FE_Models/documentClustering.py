import numpy as np
import matplotlib.pyplot as plt
from Traditional_FE_Models.cosineSimilarity import *
from scipy.cluster.hierarchy import dendrogram, linkage
from Traditional_FE_Models.tfidf import get_tfidf_TfidfVectorizer


def plot_dendrogram(corpus):
    # Compute cosine similarity using the TF-IDF vectors
    tfidf_matrix = get_tfidf_TfidfVectorizer(corpus) # tfidf_vectorizer.fit_transform(corpus)
    similarity_matrix = calculate_cosine_similarity(tfidf_matrix)

    # Perform hierarchical clustering
    # Create a DataFrame to visualize the linkage matrix
    # Display the linkage matrix
    Z = linkage(similarity_matrix, 'ward')
    df = pd.DataFrame(Z, columns=['Document/Cluster 1', 'Document/Cluster 2', 'Distance', 'Cluster Size'], dtype='object')
    print("Linkage Matrix:")
    print(df)

    # Plot the dendrogram
    plt.figure(figsize=(8, 5))
    dendrogram(Z, labels=corpus)
    plt.xticks(fontsize=8, rotation=10)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Documents/Clusters')
    plt.ylabel('Distance')
    plt.show()