from wordnet_functions import get_synonyms, get_hypernyms

if __name__ == "__main__":
    input_word = "idiot"

    synonyms = get_synonyms(input_word)
    print(f"Synonyms of '{input_word}': {synonyms}")

    hypernyms = get_hypernyms(input_word)
    print(f"Hypernyms of '{input_word}': {hypernyms}")

