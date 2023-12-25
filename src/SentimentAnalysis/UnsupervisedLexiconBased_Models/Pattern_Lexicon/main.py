from pattern.en import sentiment

def analyze_sentiment(text):
    polarity, subjectivity = sentiment(text)
    return polarity, subjectivity

hardcoded_text = "I love using Python for programming. It's such a powerful and versatile language!"

polarity, subjectivity = analyze_sentiment(hardcoded_text)

print(f"Sentiment Analysis Results:")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")

