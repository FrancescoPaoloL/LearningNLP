from sklearn.feature_extraction.text import TfidfVectorizer

# for example we use tf-idf technique
def extract_features(normalized_documents):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(normalized_documents)
    return features

