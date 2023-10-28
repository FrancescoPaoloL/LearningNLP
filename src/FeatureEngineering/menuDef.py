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
import numpy as np

from Advanced_FE_Models.word2vec import *
from Advanced_FE_Models.word_embeddings import *
from Advanced_FE_Models.text_processing import *
from sklearn.metrics.pairwise import cosine_similarity


def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_menu(corpus, labels, matrices):
    clearScreen()
    print("Choose an option:")
    print("TRADITIONAL FEATURE ENGINEERING MODELS")
    print("1. Basic feature engineer" \
              "\tLoad and preprocess data\n" \
              "\tBag of Words Model (sparse matrix)\n" \
              "\tBag of N-Grams Model\n" \
              "\tTF-IDF Model (Using CountVectorized)\n" \
              "\tTF-IDF Model (Using TfidfVectorizer)\n")
    print("2. Extract new features into TF-IDF Matrix")
    print("3. Calculate Cosine Similarity")
    print("4. Plot Dendrogram")
    print("5. LDA\n")
    print("ADVANCED FEATURE ENGINEERING MODELS")
    print("6. Word2Vec example")
    print("7. CBOW example")
    print("8. Skip-Gram example")
    print("9. Gensim example")
    print("10. Glove example\n")
    #...
    print("------------------------------------")
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
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # LDA example
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    results = lda_topic_modeling(corpus, labels)
    print("LDA Topic Distribution for Each Document:")
    print(results)
    input("Press Enter to continue...")

def word2vec_example(corpus):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Word2Vec example
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    word2vec_operations(corpus)
    input("Press Enter to continue...")

def CBOW_example():
    words, tokenizer = tokenize_and_preprocess_text()
    X, Y = generate_cbow_data(words, tokenizer)

    i = 0
    for context_index, target_index in zip(X, Y):
        context_word = tokenizer.index_word[context_index]
        target_word = tokenizer.index_word[target_index]

        print('Context (X):', context_word, '-> Target (Y):', target_word)

        if i == 15:
            break
        i += 1

    model = train_cbow_model(X, Y, tokenizer.word_index)

    # The word embeddings are learned as a result of training this model. 
    # You can obtain these embeddings using the get_word_embeddings function, 
    # which extracts the weights of the Embedding layer
    word_embeddings = get_word_embeddings(model)

    print(word_embeddings)
    input("Press Enter to continue...")


def SkipGram_example():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # SkipGram example
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    words, tokenizer = tokenize_and_preprocess_text()
    X, Y = generate_skipgram_data(words, tokenizer)

    i = 0
    for target_index, context_index in zip(X, Y):
        target_word = tokenizer.index_word[target_index]
        context_word = tokenizer.index_word[context_index]

        print('Target (X):', target_word, '-> Context (Y):', context_word)

        if i == 15:
            break
        i += 1

    model = train_skipgram_model(X, Y, tokenizer.word_index)

    word_embeddings = get_word_embeddings(model)

    print(word_embeddings)
    input("Press Enter to continue...")


def Gensim_example(vector_size=100, window=5, sg=0, min_count=5):
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Gensim example
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    words, tokenizer = tokenize_and_preprocess_text()

    print(f"Total words in corpus: {len(words)}")
    print(f"Sample of tokenized words: {words[:10]}")

    word2vec_model = train_gensim_word2vec([words], vector_size=vector_size, window=window, sg=sg, min_count=min_count)
    word_embeddings = get_gensim_word_embeddings(word2vec_model)

    # Find similar words to a given word
    target_word = "king"
    similar_words = word_embeddings.most_similar(target_word, topn=5)
    print(f"Words similar to '{target_word}':")
    for word, similarity in similar_words:
        print(f"{word}: {similarity:.2f}")
    input("Press Enter to continue...")


def Glove_example():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Glove example
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    words, tokenizer = tokenize_and_preprocess_text()

    # we use CBOW with GloVe because:
    #   - CBOW focuses on nearby words for word meanings, while 
    #   - GloVe analyzes word relationships in a larger context
    # So using both approaches combines local and global context, 
    # potentially enhancing word embeddings.
    X, Y = generate_cbow_data(words, tokenizer)

    embedding_dim = 300
    num_epochs = 10
    glove_model = train_custom_word_embeddings(X, Y, tokenizer.word_index, embedding_dim, num_epochs)

    word_embeddings_glove = get_word_embeddings(glove_model)

    # check if a specific word ("king" in this case) is in the custom 
    # GloVe model's vocabulary
    word_to_check = "king"
    if word_to_check in tokenizer.word_index:
        word_index = tokenizer.word_index[word_to_check]
        vector_glove = word_embeddings_glove[word_index]
        print(f"Custom Glove vector for '{word_to_check}': {vector_glove}")
    else:
        print(f"'{word_to_check}' not found in the tokenizer.")

    # Perform word similarity or analogy tasks
    # For example we calculate how similar "king" and "queen" are in relation to "woman" 
    # using custom GloVe embeddings
    word1 = "king"
    word2 = "queen"
    word3 = "woman"

    if word1 in tokenizer.word_index and word2 in tokenizer.word_index and word3 in tokenizer.word_index:
        vector1 = word_embeddings_glove[tokenizer.word_index[word1]]
        vector2 = word_embeddings_glove[tokenizer.word_index[word2]]
        vector3 = word_embeddings_glove[tokenizer.word_index[word3]]

        
        # if the three words exist in the model's vocabulary 
        # then it measures cosine similarity between word vectors
        similarity = cosine_similarity([vector1 - vector3], [vector2 - vector3])
        print(f"Similarity between '{word1}' and '{word2}' (analogous to '{word3}') using Custom GloVe: {similarity[0][0]}")
    else:
        print("Some words not found in the tokenizer for the similarity task.")

    input("Press Enter to continue...")
