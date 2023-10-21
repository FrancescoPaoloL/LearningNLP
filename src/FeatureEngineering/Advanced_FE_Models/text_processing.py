from Advanced_FE_Models.download_text import download_gutenberg
from nltk.tokenize import word_tokenize
from keras.preprocessing.text import Tokenizer

def tokenize_and_preprocess_text():
    hamlet = download_gutenberg("shakespeare-hamlet.txt")
    words = word_tokenize(hamlet.lower())
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([words])
    return words, tokenizer
