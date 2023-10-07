from spelling_correction import correct_text
from stemmers import stem_words

def main():
    print("\nExample text with some spelling errors".upper())
    text_with_errors = "Ths is an exmple of text witg spelking mistkes. How ar you doin?"
    print(text_with_errors)
    corrected_text = correct_text(text_with_errors)
    print(corrected_text)

    print("\nstemming examples".upper())
    print(stem_words('jumping'))  # Using Porter Stemmer for English
    print(stem_words('springen', 'german'))  # Using Snowball Stemmer for German

if __name__ == "__main__":
    main()
