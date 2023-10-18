import os
import platform
from data_preprocessing import load_and_preprocess_data, text_preprocessing
from Traditional_FE_Models.bagOfWords import get_bag_of_words
from Traditional_FE_Models.bagOfNgrams import get_bag_of_ngrams
from Traditional_FE_Models.tfidf import get_tfidf_CountVectorizer, get_tfidf_TfidfVectorizer
from Traditional_FE_Models.tfidfVectorization import generate_tfidf_matrix
from Traditional_FE_Models.cosineSimilarity import *
from Traditional_FE_Models.documentClustering import *
from Traditional_FE_Models.LDA import *

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_menu(corpus, labels, matrices):
    clearScreen()
    print("Choose an option:")
    print("1. Basic feature engineer" \
              "\tLoad and preprocess data\n" \
              "\tBag of Words Model (sparse matrix)\n" \
              "\tBag of N-Grams Model\n" \
              "\tTF-IDF Model (Using CountVectorized)\n" \
              "\tTF-IDF Model (Using TfidfVectorizer)\n")
    print("2. Extract new features into TF-IDF Matrix\n")
    print("3. Calculate Cosine Similarity\n")
    print("4. Plot Dendrogram\n")
    print("5. LDA\n")
    print("0. Exit\n")

def bags(corpus, labels):
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
    input("Press Enter to continue...")

def extracting_features(corpus):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # extracting features for new documents
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tfidf_matrix = generate_tfidf_matrix(corpus)

    print("Extracting new features into TF-IDF Matrix:")
    print(tfidf_matrix)
    input("Press Enter to continue...")


def documents_similarity(matrices):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # documents similarity
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    input("Press Enter to continue...")

def documents_clustering(corpus):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # documents clustering in dendrogram
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    plot_dendrogram(corpus)
    input("Press Enter to continue...")

def LDA_algorithm(corpus, labels):
    results = lda_topic_modeling(corpus, labels)
    print("LDA Topic Distribution for Each Document:")
    print(results)
    input("Press Enter to continue...")