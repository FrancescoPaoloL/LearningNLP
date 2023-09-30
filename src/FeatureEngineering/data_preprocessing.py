'''
This code defines functions to load a collection of text documents 
along with their labels into a structured DataFrame and then 
preprocesses the text data by removing stopwords, non-alphabetical 
characters, and converting it to lowercase for further analysis or 
machine learning tasks.
'''

import pandas as pd
import numpy as np
import re
import nltk

def load_and_preprocess_data(corpus, labels):
    pd.options.display.max_colwidth = 200

    corpus = np.array(corpus)
    corpus_df = pd.DataFrame({"Document": corpus, "Category": labels})
    corpus_df = corpus_df[["Document", "Category"]]
    
    return corpus_df

def text_preprocessing(corpus_df):
    wpt = nltk.WordPunctTokenizer()
    stop_words = nltk.corpus.stopwords.words("english")

    def normalize_document(doc):
        doc = re.sub(r"[^a-zA-Z\s]", "", doc, re.I | re.A)
        doc = doc.lower()
        doc = doc.strip()
        tokens = wpt.tokenize(doc)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        doc = " ".join(filtered_tokens)
        return doc

    normalize_corpus = np.vectorize(normalize_document)
    norm_corpus = normalize_corpus(corpus_df["Document"])
    
    return norm_corpus
