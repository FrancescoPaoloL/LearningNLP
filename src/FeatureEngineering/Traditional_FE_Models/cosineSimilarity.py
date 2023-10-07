import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_cosine_similarity(matrix1, matrix2):
    similarity_matrix = cosine_similarity(matrix1, matrix2)
    similarity_df = pd.DataFrame(similarity_matrix)
    return similarity_df


def calculate_cosine_similarity_from_scratch(matrix1, matrix2):
    dot_product = np.dot(matrix1.flatten(), matrix2.flatten())
    norm1 = np.linalg.norm(matrix1)
    norm2 = np.linalg.norm(matrix2)
    similarity = dot_product / (norm1 * norm2)
    return similarity