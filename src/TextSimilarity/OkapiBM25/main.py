import math
from collections import Counter
from bm25 import calculate_idf, calculate_bm25_score, rank_documents

K1 = 1.5
B = 0.75
K3 = 1
SMOOTHING_CONSTANT = 0.5

if __name__ == "__main__":
    documents = [
        "The quick brown fox jumps over the lazy dog.",
        "A quick brown dog outpaces a lazy fox.",
        "The lazy dog sleeps all day."
    ]

    avg_len = sum(len(doc.split()) for doc in documents) / len(documents)
    idf = calculate_idf(documents)

    query = "quick brown fox"
    result = rank_documents(documents, query, idf, avg_len)

    print("IDF values:")
    for term, value in idf.items():
        print("{}: {}".format(term, value))

    print("\nBM25 Scores for the query '{}':".format(query))
    for idx, score in result:
        print("Document {}: {}".format(idx + 1, score))

