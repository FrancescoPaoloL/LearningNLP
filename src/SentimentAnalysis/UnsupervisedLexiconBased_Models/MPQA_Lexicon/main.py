import os

def load_mpqa_lexicon(lexicon_file):
    lexicon = {}
    try:
        # Print the provided file path
        print("Provided File Path:", lexicon_file)

        # Check if the file exists
        if not os.path.exists(lexicon_file):
            print("Error: Lexicon file does not exist.")
            return lexicon

        # Print the real path to the file
        real_path = os.path.realpath(lexicon_file)
        print("Real Path to File:", real_path)

        with open(lexicon_file, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                #print(f"Processing line {line_number}: {line.strip()}")
                if "word1=" in line:
                    parts = line.strip().split()
                    for part in parts:
                        if part.startswith("word1="):
                            word = part[6:]
                        elif part.startswith("priorpolarity="):
                            polarity = part[14:]
                            lexicon[word] = polarity
                            break
    except Exception as e:
        print("Error loading lexicon:", e)
    return lexicon

def get_word_sentiment(word, lexicon):
    return lexicon.get(word, "unknown")

def analyze_sentiment(sentence, lexicon):
    words = sentence.lower().split()
    sentiment_scores = [get_word_sentiment(word, lexicon) for word in words]
    return sentiment_scores

if __name__ == "__main__":
    print("Working Directory:", os.getcwd())

    # downloaded from http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/
    lexicon_file = "../../lexicon/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff"
    print("Lexicon File Path:", lexicon_file)

    lexicon = load_mpqa_lexicon(lexicon_file)

    # Print the loaded lexicon (for debugging purposes)
    #print("Loaded Lexicon:", lexicon)

    sentence = "Great example using Lexicon Python"
    sentiment_scores = analyze_sentiment(sentence, lexicon)

    print("Sentence:", sentence)
    print("Sentiment Scores:", sentiment_scores)
