import nltk

def tokenize_text(text):
    return [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]

def perform_pos_tagging(words):
    return nltk.pos_tag(words)

def perform_ne_chunking(pos_tags):
    return nltk.ne_chunk(pos_tags)
