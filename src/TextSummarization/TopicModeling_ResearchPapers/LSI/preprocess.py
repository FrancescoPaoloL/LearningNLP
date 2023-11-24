from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing import strip_punctuation, strip_numeric

def preprocess_documents(papers_content):
    return [
        strip_numeric(strip_punctuation(remove_stopwords(doc))).split()
        for doc in papers_content
    ]

