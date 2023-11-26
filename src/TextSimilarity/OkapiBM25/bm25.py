import math
from collections import Counter

K1 = 1.5
B = 0.75
K3 = 1
SMOOTHING_CONSTANT = 0.5

def calculate_idf(documents):
    doc_count = len(documents)
    idf = {}
    all_terms = set(term for doc in documents for term in doc.split())

    for term in all_terms:
        doc_count_with_term = sum(1 for doc in documents if term in doc)
        idf[term] = math.log((doc_count - doc_count_with_term + SMOOTHING_CONSTANT) / (doc_count_with_term + SMOOTHING_CONSTANT) + 1.0)

    return idf

def calculate_bm25_score(query, doc, idf, avg_len, k1=K1, b=B, k3=K3):
    doc_len = len(doc.split())
    doc_term_freq = Counter(doc.split())
    
    score = 0

    for term in query.split():
        if term in doc_term_freq:
            tf = doc_term_freq[term]
        else:
            tf = 0

        idf_value = idf.get(term, 0)
        term_count_in_query = query.split().count(term)

        n = tf * (k1 + 1)
        d = tf + k1 * (1 - b + b * (doc_len / avg_len))
        q = k3 + term_count_in_query
        if d > 0 and q > 0:
            score += (n / d) * idf_value * ((k3 + 1) * term_count_in_query) / q

    return score

def rank_documents(documents, query, idf, avg_len):
    scores = [
        (idx, calculate_bm25_score(query, doc, idf, avg_len))
        for idx, doc in enumerate(documents)
    ]
    return sorted(scores, key=lambda x: x[1], reverse=True)

