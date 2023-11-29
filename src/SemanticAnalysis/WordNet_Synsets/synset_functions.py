import nltk
from nltk.corpus import wordnet

def explore_synsets(word):
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for the word '{word}'.")
        return

    print(f"Synsets for the word '{word}':")

    for synset in synsets:
        print(f"\nSynset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"POS (Part of Speech): {synset.pos()}")

        # Examples of word usage in the synset
        examples = synset.examples()
        if examples:
            print("Examples:")
            for example in examples:
                print(f"- {example}")

        # Hypernyms (more abstract terms)
        hypernyms = synset.hypernyms()
        if hypernyms:
            print("\nHypernyms:")
            for hypernym in hypernyms:
                print(f"- {hypernym.name()}")

        # Hyponyms (more specific terms)
        hyponyms = synset.hyponyms()
        if hyponyms:
            print("\nHyponyms:")
            for hyponym in hyponyms:
                print(f"- {hyponym.name()}")

        print("\n" + "="*40)

