from nltk.corpus import wordnet

def get_related_words(word, relationship):
    related_words = []

    for syn in wordnet.synsets(word):
        if relationship == 'synonyms':
            related_words.extend(lemma.name() for lemma in syn.lemmas())
        elif relationship == 'hypernyms':
            related_words.extend(hypernym.name() for hypernym in syn.hypernyms())
    return list(set(related_words))

