from gensim import corpora
from gensim.models import LsiModel

def build_lsi_model(preprocessed_documents, num_topics=5):
    dictionary = corpora.Dictionary(preprocessed_documents)
    corpus = [dictionary.doc2bow(doc) for doc in preprocessed_documents]
    return LsiModel(corpus, id2word=dictionary, num_topics=num_topics)

