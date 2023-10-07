import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_tfidf_matrix(documents):
    # Initialize the TfidfVectorizer with custom options
    tv = TfidfVectorizer(
        stop_words='english',
        max_features=10,
        ngram_range=(1, 2)
    )

    # Fit and transform the documents into a TF-IDF matrix
    tfidf_matrix = tv.fit_transform(documents)

    # Get the feature names (terms)
    feature_names = tv.get_feature_names()

    # Convert the TF-IDF matrix into a DataFrame
    tfidf_df = pd.DataFrame(np.round(tfidf_matrix.toarray(), 2),  columns=feature_names)
    
    return tfidf_df
