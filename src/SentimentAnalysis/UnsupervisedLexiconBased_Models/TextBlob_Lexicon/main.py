from textblob import TextBlob

sample_text = "NLP is awesome for make life better!"
blob = TextBlob(sample_text)

sentiment_polarity = blob.sentiment.polarity
sentiment_subjectivity = blob.sentiment.subjectivity

print(f"Text: {sample_text}")
print(f"Sentiment Polarity: {sentiment_polarity}")
print(f"Sentiment Subjectivity: {sentiment_subjectivity}")

lexicon_entries = blob.sentiment_assessments.assessments
print("\nLexicon Entries:")
for entry in lexicon_entries:
    print(f"{entry[0][0]}: {entry[1]}")

