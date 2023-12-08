import nltk
from nltk.corpus import opinion_lexicon
from nltk.tokenize import word_tokenize

nltk.download('opinion_lexicon')
nltk.download('punkt')

# Load Bing Liu's opinion lexicon
positive_words = set(opinion_lexicon.positive())
negative_words = set(opinion_lexicon.negative())

def analyze_sentiment(text):
    words = word_tokenize(text.lower())
    num_positive = sum(1 for word in words if word in positive_words)
    num_negative = sum(1 for word in words if word in negative_words)

    if num_positive > num_negative:
        return "Positive"
    elif num_positive < num_negative:
        return "Negative"
    else:
        return "Neutral"

text_to_analyze = "I was really bored when I watched the movie."
sentiment_result = analyze_sentiment(text_to_analyze)
print(f"Sentiment: {sentiment_result}")

