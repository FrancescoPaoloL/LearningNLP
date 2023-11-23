import nltk
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    normalized_tokens = [word for word in tokens if word.isalnum()]
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in normalized_tokens if word not in stop_words]
    return filtered_tokens

def extract_collocations(tokens):
    finder = BigramCollocationFinder.from_words(tokens)
    bigram_measures = BigramAssocMeasures()
    return finder.nbest(bigram_measures.pmi, 10)

