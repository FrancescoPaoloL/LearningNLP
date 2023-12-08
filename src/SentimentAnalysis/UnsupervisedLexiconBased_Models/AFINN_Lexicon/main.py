import re

def load_afinn():
    afinn = {}
    # downloaded from https://github.com/fnielsen/afinn/blob/master/afinn/data/afinn-111.txt
    with open("../../lexicon/AFINN-111.txt", 'r') as afinn_file:
        for line in afinn_file:
            term, score = line.strip().split('\t')
            afinn[term] = int(score)
    return afinn

def sentiment_analysis(text, afinn):
    words = re.findall(r'\b\w+\b', text.lower())
    sentiment_score = sum(afinn.get(word, 0) for word in words)
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    afinn_lexicon = load_afinn()
    input_text = "I love this product! It's amazing."
    sentiment = sentiment_analysis(input_text, afinn_lexicon)
    print(f"The sentence '{input_text}' has sentiment {sentiment}!")

