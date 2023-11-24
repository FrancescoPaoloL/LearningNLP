from gensim import corpora
from gensim.models import LdaModel

def build_lda_model(corpus, dictionary, num_topics):
    lda_model = LdaModel(corpus, id2word=dictionary, num_topics=num_topics)
    return lda_model

