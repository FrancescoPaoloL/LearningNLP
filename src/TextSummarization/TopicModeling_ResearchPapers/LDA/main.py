from gensim import corpora  # Add this import statement
from preprocess import preprocess_documents
from build_model import build_lda_model

def main():
    tgz_path = '../papers/nips12raw_str602.tgz'
    preprocessed_documents = preprocess_documents(tgz_path)

    dictionary = corpora.Dictionary(preprocessed_documents)
    corpus = [dictionary.doc2bow(doc) for doc in preprocessed_documents]

    num_topics = 5
    lda_model = build_lda_model(corpus, dictionary, num_topics)

    print("\nLDA Topics:")
    print(lda_model.print_topics())

    new_document_index = 0
    new_bow = corpus[new_document_index]
    new_lda = lda_model[new_bow]

    print("\nLDA representation of the new document:")
    print(new_lda)

if __name__ == "__main__":
    main()

