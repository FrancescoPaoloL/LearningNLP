from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
import pandas as pd
import numpy as np

def get_tfidf_CountVectorizer(corpus):
    # CountVectorizer is used to convert text data into 
    # a matrix that represents the raw requency of words (terms) 
    # in the documents.
    cv = CountVectorizer(min_df=0., max_df=1.)
    cv_matrix = cv.fit_transform(corpus)
    cv_matrix = cv_matrix.toarray()

    # TfidfTransformer is used to transform the word frequency 
    # matrix into a TF-IDF matrix.
    # TF-IDF(term, document) = TF(term, document) * IDF(term)
    tt = TfidfTransformer(norm="l2", use_idf=True, smooth_idf=True)
    tt_matrix = tt.fit_transform(cv_matrix)

    # This line converts the TF-IDF matrix into a NumPy array.
    tt_matrix = tt_matrix.toarray()

    # This line gets the list of unique terms (words) 
    # found in the documents.
    vocab = cv.get_feature_names()
    
    tfidf_df = pd.DataFrame(np.round(tt_matrix, 2), columns=vocab)

    return tfidf_df

def get_tfidf_TfidfVectorizer(corpus):
    # TfidfVectorizer is an all-in-one tool that directly 
    # takes a corpus of text as input and internally computes 
    # both the term frequencies and TF-IDF values. 
    # you can explicit he normalization type, for example.
    tv = TfidfVectorizer(min_df=0., max_df=1., norm='l2',
                         use_idf=True, smooth_idf=True)
    tv_matrix = tv.fit_transform(corpus)
    tv_matrix = tv_matrix.toarray()

    vocab = tv.get_feature_names()
    tfidf_df = pd.DataFrame(np.round(tv_matrix, 2), columns=vocab)

    return tfidf_df
