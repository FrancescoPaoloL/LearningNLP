from gensim.models import Word2Vec

def word2vec_operations(corpus):
    tokenized_corpus = [sentence.lower().split() for sentence in corpus]
    model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, sg=0)

    # Find the vector representation of a word
    target_word = 'sun'
    word_vector = model.wv[target_word]
    print(f"Vector representation of the word '{target_word}':")
    print(word_vector)

    # Find similar words
    similar_words = model.wv.most_similar(target_word, topn=3)
    print(f"Words similar to '{target_word}':")
    for word, similarity in similar_words:
        print(f"{word}: Similarity = {similarity:.2f}")
