import nltk
from wordnet_functions import get_synonyms, get_hypernyms
from synset_functions import explore_synsets

if __name__ == "__main__":
    nltk.download('wordnet')
    input_word = "nerd"

    synonyms = get_synonyms(input_word)
    print(f"Synonyms of '{input_word}': {synonyms}")

    hypernyms = get_hypernyms(input_word)
    print(f"Hypernyms of '{input_word}': {hypernyms}")

    explore_synsets(input_word)

