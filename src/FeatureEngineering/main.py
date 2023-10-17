"""
We need a text ccorpus to work on and demostrate different feature engineering an representation methodologies.
To keep thing simple, we bult a short and simple text corpus.

This code loads and preprocesses some text data, then creates three different models 
to represent the text: Bag of Words, Bag of N-Grams, and TF-IDF, and finally, it 
prints the results of each model.

"""

from data_preprocessing import load_and_preprocess_data, text_preprocessing
from Traditional_FE_Models.bagOfWords import get_bag_of_words
from Traditional_FE_Models.bagOfNgrams import get_bag_of_ngrams
from Traditional_FE_Models.tfidf import get_tfidf_CountVectorizer, get_tfidf_TfidfVectorizer
from Traditional_FE_Models.tfidfVectorization import generate_tfidf_matrix
import numpy as np
from Traditional_FE_Models.cosineSimilarity import *
from Traditional_FE_Models.documentClustering import *


def main():
    # Define 'corpus' and its associated labels
    corpus = ["The sun sets over the horizon, painting the sky with colors.",
            "Surfers ride the waves as dolphins swim nearby.",
            "In the depths of the forest, birds chirp and leaves rustle.",
            "Gourmet chefs prepare exquisite dishes with precision and creativity.",
            "Children play in the park, laughing and enjoying the sunshine.",
            "The city streets are bustling with people, cars, and music.",
            "A lone hiker explores the rugged mountain terrain.",
            "Artists express their emotions through paintings and sculptures."]

    labels = ["nature", "nature", "nature", "food", "family", "city", "adventure", "art"]


    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    # just preliminary things
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    corpus_df = load_and_preprocess_data(corpus, labels)
    print("Load and preprocess data")
    print(corpus_df)

    norm_corpus = text_preprocessing(corpus_df)
    print("\nShow nornalized data")
    print(norm_corpus)

    #~~~~~~~~~~~~~~~~~~~~
    # a naive approach
    #~~~~~~~~~~~~~~~~~~~~
    bag_of_words_df = get_bag_of_words(norm_corpus)
    print("\nUsing Bag of Words Model (as sparse matrix):")
    print(bag_of_words_df)

    # In this code, for sake of simplicity, we create a representation of text data in terms 
    # of bigrams (2-grams).
    bag_of_ngrams_df = get_bag_of_ngrams(norm_corpus, 2, 2)
    print("\nUsing Bag of N-Grams Model:")
    print(bag_of_ngrams_df)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # it's better do something clever
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tfidf_df_old = get_tfidf_CountVectorizer(norm_corpus)
    print("\nTF-IDF Model (Using CountVectorized):")
    print(tfidf_df_old)

    tfidf_df_new = get_tfidf_TfidfVectorizer(norm_corpus)
    print("\nTF-IDF Model (Using TfidfVectorizer, in practice, yields the same result.):")
    print(tfidf_df_new)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # extracting features for new documents
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tfidf_matrix = generate_tfidf_matrix(corpus)

    print("Extracting new features into TF-IDF Matrix:")
    print(tfidf_matrix)


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # documents similarity
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    matrices = [
        {
            "name": "\nSimilar Matrices",
            "matrix1": np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]),
            "matrix2": np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])
        },
        {
            "name": "\nNot Similar Matrices",
            "matrix1": np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]),
            "matrix2": np.array([[9, 8, 7],
                                [6, 5, 4],
                                [3, 2, 1]])
        },
        {
            "name": "\nVarying Matrices",
            "matrix1": np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]),
            "matrix2": np.array([[2, 3, 4],
                                [5, 6, 7],
                                [8, 9, 10]])
        }
    ]

    for matrix_data in matrices:
        matrix1 = matrix_data["matrix1"]
        matrix2 = matrix_data["matrix2"]
        similarity = calculate_cosine_similarity(matrix1, matrix2)
        
        print(f"{matrix_data['name']}:")
        print(f"Matrix 1:\n{matrix1}")
        print(f"Matrix 2:\n{matrix2}")
        print(f"Cosine Similarity:\n{similarity}\n")

    for matrix_data in matrices:
        matrix1 = matrix_data["matrix1"]
        matrix2 = matrix_data["matrix2"]
        
        # Using the first version of the function
        similarity_v1 = calculate_cosine_similarity(matrix1, matrix2)
        
        # Using the second version of the function
        similarity_v2 = calculate_cosine_similarity_from_scratch(matrix1, matrix2)
        
        print(f"{matrix_data['name']}:")
        print(f"\nMatrix 1:\n{matrix1}")
        print(f"\nMatrix 2:\n{matrix2}")
        print(f"\nCosine Similarity (library version):\n{similarity_v1}")
        # Calculate the average similarity value
        average_similarity = similarity_v1.mean().mean()

        print(f"\nAverage Cosine Similarity: {average_similarity}")
        print(f"\nCosine Similarity (from scratch version): {similarity_v2}\n\n")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # documents clustering in dendrogram
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    plot_dendrogram(corpus[:4])

if __name__ == "__main__":
    main()