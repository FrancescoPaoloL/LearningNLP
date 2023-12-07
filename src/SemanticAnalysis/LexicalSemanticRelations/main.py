import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def find_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

target_word = 'drop'
synonyms = find_synonyms(target_word)

if synonyms:
    print(f"Synonyms for '{target_word}': {', '.join(synonyms)}")
else:
    print(f"No synonyms found for '{target_word}'.")

