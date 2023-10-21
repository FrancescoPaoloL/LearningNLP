import nltk
from nltk.corpus import gutenberg

def download_gutenberg(text):
    nltk.download('gutenberg')
    return gutenberg.raw(text)