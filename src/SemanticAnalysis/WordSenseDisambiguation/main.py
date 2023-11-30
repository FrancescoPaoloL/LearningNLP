import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

sentence = "I saw a bat flying in the night sky and thought about my favorite baseball bat."
tokens = word_tokenize(sentence)
# Choose the ambiguous word (in this case, "bat")
ambiguous_word = "bat"

# Get all possible synsets for the word "bat"
synsets = wordnet.synsets(ambiguous_word)
for synset in synsets:
    print(f"Synset: {synset}")
    print(f"Definition: {synset.definition()}")
    print()

