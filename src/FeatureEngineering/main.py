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
from Traditional_FE_Models.tfidfExtratingNewFeatures import generate_tfidf_matrix


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