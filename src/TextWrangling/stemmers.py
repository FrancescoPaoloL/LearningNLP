from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer

def stem_words(word, language="english"):
    stemmers = {
        "porter": PorterStemmer(),
        "lancaster": LancasterStemmer(),
        "regexp": RegexpStemmer('ing$|s$|ed$', min=4),
        "snowball": SnowballStemmer(language),
    }

    if language not in SnowballStemmer.languages:
        print(f"Snowball Stemmer does not support {language}. Defaulting to English.")

    if language == "german":
        return stemmers["snowball"].stem(word)
    else:
        return stemmers["porter"].stem(word)
