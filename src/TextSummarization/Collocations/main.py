from nltk.corpus import gutenberg
from operator import itemgetter
from nlp_utils import preprocess_text, extract_collocations

def download_nltk_resources():
    import nltk
    nltk.download("punkt")
    nltk.download("stopwords")

def main():
    # Download NLTK resources
    download_nltk_resources()

    # Load "The Great Gatsby" text from Gutenberg
    gatsby = gutenberg.raw("burgess-busterbrown.txt")

    # Tokenize and normalize the text
    filtered_tokens = preprocess_text(gatsby)

    # Extract bigrams
    collocations = extract_collocations(filtered_tokens)

    # Display collocations
    for collocation in collocations:
        print(' '.join(collocation))

    # Sort collocations by frequency
    from nltk import FreqDist
    fdist = FreqDist(collocations)
    sorted_collocations = sorted(fdist.items(), key=itemgetter(1), reverse=True)

    # Display sorted collocations
    print("\nTop Collocations:")
    for collocation, frequency in sorted_collocations:
        print(f"{collocation}: {frequency}")

if __name__ == "__main__":
    main()

