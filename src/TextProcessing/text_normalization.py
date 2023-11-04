from sklearn.feature_extraction.text import CountVectorizer
import re
import string

# As "Normalization" we remove 
# only punctuation and lowercase
def normalize_text(documents):
    normalized_documents = []

    for document in documents:
        text = re.sub(f"[{re.escape(string.punctuation)}]", " ", document.lower())
        normalized_documents.append(text)

    return normalized_documents

