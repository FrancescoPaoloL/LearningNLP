from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('sentiwordnet')

def get_sentiment_score(word, pos):
    synsets = list(swn.senti_synsets(word, pos=pos))
    if not synsets:
        return 0.0, 0.0
    
    pos_score = sum(s.pos_score() for s in synsets) / len(synsets)
    neg_score = sum(s.neg_score() for s in synsets) / len(synsets)
    
    return pos_score, neg_score

def get_sentence_sentiment(sentence):
    tokens = word_tokenize(sentence)
    sentiment_scores = {'pos': 0.0, 'neg': 0.0}
    
    # Create a dictionary where keys are POS tags, 
    # and values are their corresponding SentiWordNet POS tags. 
    # In this case: 
    #   'N' (noun) is mapped to 'n', 
    # 'V' (verb) is mapped to 'v', 
    #'R' (adverb) is mapped to 'r', and 
    #'J' (adjective) is mapped to 'a'
    for token, pos in nltk.pos_tag(tokens):
        senti_pos = pos[0].upper()
        senti_pos = {'N': 'n', 'V': 'v', 'R': 'r', 'J': 'a'}.get(senti_pos, 'n')
        
        pos_score, neg_score = get_sentiment_score(token, senti_pos)
        
        sentiment_scores['pos'] += pos_score
        sentiment_scores['neg'] += neg_score

    return sentiment_scores


sentence = "I love programming and enjoy learning new things!"
sentiment_scores = get_sentence_sentiment(sentence)

print("\nSentiment Scores:")
print(f"Positive: {sentiment_scores['pos']:.2f}")
print(f"Negative: {sentiment_scores['neg']:.2f}")

overall_sentiment = "Positive" if sentiment_scores['pos'] > sentiment_scores['neg'] else "Negative" if sentiment_scores['pos'] < sentiment_scores['neg'] else "Neutral"
print(f"Overall sentiment: {overall_sentiment}")

