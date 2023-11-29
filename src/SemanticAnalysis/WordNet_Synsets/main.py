import nltk
from wordnet_functions import get_related_words
from synset_functions import explore_synsets

if __name__ == "__main__":
    nltk.download('wordnet')
    input_word = "nerd"

    # Get synonyms of the input word
    synonyms = get_related_words(input_word, 'synonyms')
    print(f"Synonyms of '{input_word}': {synonyms}")

    # Get hypernyms of the input word
    hypernyms = get_related_words(input_word, 'hypernyms')
    print(f"Hypernyms of '{input_word}': {hypernyms}")

    explore_synsets(input_word)

