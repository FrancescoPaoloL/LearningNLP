## [Information Retrieval]

[return to readme](../readme.md)

### Okapi BM25 Ranking Formula
The Okapi BM25 ranking formula is used to score the relevance of a document to a given search query. It is commonly employed in information retrieval systems.
It is defined as:

$$ \text{BM25}(D, Q) = \sum_{i=1}^{n} \frac{{f(q_i, D) \cdot (k_1 + 1)}}{{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{{\text{dl}(D)}}{{\text{avgdl}}}\right)}} \cdot \log\left(\frac{{N - n(q_i) + 0.5}}{{n(q_i) + 0.5}}\right) \cdot \frac{{(k_2 + 1) \cdot qf(q_i, Q)}}{{k_2 + qf(q_i, Q)}} $$
 
This formula calculates a score representing the relevance of the document to the query, taking into account the frequency of query terms in the document and their overall distribution in the document collection.
The script make output that represents the BM25 scores for each document in the provided collection based on the given query, "quick brown fox." 
For example we get:

    Document 1: "The quick brown fox jumps over the lazy dog."
        BM25 Score: 1.3076713878207966

    Document 2: "A quick brown dog outpaces a lazy fox."
        BM25 Score: 0.9219687396718056

    Document 3: "The lazy dog sleeps all day."
        BM25 Score: 0.0

As you can see, Document 1 contains all the terms from the query ("quick," "brown," and "fox"), so it has the higher score. On the opposite, Document 3 has a BM25 score of 0.0 because it doesn't contain any of the terms from the query. 

[Back to top](#)

[return to readme](../readme.md)