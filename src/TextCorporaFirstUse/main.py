from nltk.corpus import gutenberg
from my_nltk_utils import ensure_nltk_downloads
from my_text_processing import tokenize_text, perform_pos_tagging, perform_ne_chunking

def main():
    ensure_nltk_downloads('src/TextCorporaFirstUse/nltk_resources.yaml')

    selected_text = 'blake-poems.txt'
    text = gutenberg.raw(selected_text)

    # Tokenize the text and get the first 20 words
    sentences = tokenize_text(text)
    first_20_words = sentences[0][:20]

    # Perform POS tagging and on the first 20 words
    pos_tags = perform_pos_tagging(first_20_words)
    chunked = perform_ne_chunking(pos_tags)

    print("First 20 words:", first_20_words)
    print("\nPOS Tags:")
    print(pos_tags)
    print("\nShallow Parsing (NE Chunking):")
    print(chunked)

if __name__ == "__main__":
    main()

