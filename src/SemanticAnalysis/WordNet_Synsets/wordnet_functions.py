import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return list(set(synonyms))

def get_hypernyms(word):
    hypernyms = []
    for syn in wordnet.synsets(word):
        for hypernym in syn.hypernyms():
            hypernyms.append(hypernym.name())
    return list(set(hypernyms))

