'''
An "n-gram" model is a way of representing sequences of words or characters in a text
that consists in a contiguous sequence of n items from a given sample of text. 

In the context of natural language processing, these "items" are usually words or characters. 
The "n" in "n-gram" represents the number of items in the sequence.

Examples:
    Unigram (1-gram):
        This is the simplest form of n-gram, where each item is a single word. 
        For example, if you have the sentence "I love ice cream," the unigrams would be: "I," "love," "ice," and "cream."

    Bigram (2-gram):
        In a bigram, each item consists of two consecutive words. 
        Using the same sentence, the bigrams would be: "I love," "love ice," and "ice cream."

    Trigram (3-gram):
        A trigram consists of three consecutive words. 
        For the sentence, the trigrams would be: "I love ice" and "love ice cream."

    4-gram (Four-gram):
        In a 4-gram, each item is a sequence of four consecutive words.

The purpose of using n-grams in NLP and text analysis is to capture patterns and relationships between words in a text. 
For example, in a language model, knowing the previous two words (a trigram) can help predict the next word in a sentence.
'''


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def get_bag_of_ngrams(corpus, rangeFrom, rangeTo):
    bv = CountVectorizer(ngram_range=(rangeFrom, rangeTo))
    bv_matrix = bv.fit_transform(corpus)
    bv_matrix = bv_matrix.toarray()
    vocab = bv.get_feature_names()
    bag_of_ngrams_df = pd.DataFrame(bv_matrix, columns=vocab)
    
    return bag_of_ngrams_df
