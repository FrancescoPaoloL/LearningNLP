import math

SMOOTHING_CONSTANT = 0.5

def calculate_idf(documents):
    doc_count = len(documents)
    idf = {}
    all_terms = set(term for doc in documents for term in doc.split())

    for term in all_terms:
        doc_count_with_term = sum(1 for doc in documents if term in doc)
        idf[term] = math.log((doc_count - doc_count_with_term + SMOOTHING_CONSTANT) / (doc_count_with_term + SMOOTHING_CONSTANT) + 1.0)

    return idf

