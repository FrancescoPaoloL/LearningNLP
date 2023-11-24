from nltk.corpus import gutenberg
from operator import itemgetter
from nlp_utils import preprocess_text, extract_collocations
from nltk import FreqDist

def download_nltk_resources():
    import nltk
    nltk.download("punkt")
    nltk.download("stopwords")

def main():
    download_nltk_resources()
    gatsby = gutenberg.raw("burgess-busterbrown.txt")
    filtered_tokens = preprocess_text(gatsby)

    collocations = extract_collocations(filtered_tokens)

    # Display collocations
    for collocation in collocations:
        print(' '.join(collocation))

    # Sort collocations by frequency
    fdist = FreqDist(collocations)
    sorted_collocations = sorted(fdist.items(), key=itemgetter(1), reverse=True)

    print("\nTop Collocations:")
    for collocation, frequency in sorted_collocations:
        print(f"{collocation}: {frequency}")

if __name__ == "__main__":
    main()

