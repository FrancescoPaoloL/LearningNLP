## [Text Preprocessing]

[return to readme](../readme.md)

### Text Corpora using
This Python project demonstrates a very simple text corpus analysis using the Natural Language Toolkit (NLTK) library. To achieve this, we've implemented basic functionalities on downloading essential NLTK resources, extracting the first 20 words from Blake's poems in the Gutenberg corpus, tokenizing the text, performing Part-of-Speech (POS) tagging, and conducting named-entity chunking.
Specifically, we rely on the following NLTK components:

- <b>Tokenizers/Punkt</b>: This component is the Punkt tokenizer, a pre-trained sentence tokenizer designed to split text into individual sentences based on text patterns, such as periods, exclamation points, and question marks.
- <b>Chunkers/maxent_ne_chunker</b>: This component is responsible for Named Entity Recognition (NER), which involves identifying and categorizing named entities within the text.
- <b>Corpora/words</b>: In NLTK, this refers to a collection of words in the English language.
- <b>Pos_tag</b>: This NLTK tool is used to automatically tag words in a text with their respective parts of speech.

## [Text Wrangling]
Text wrangling is the process of cleaning your data to make it readable by your program. To demonstrate how it works, I have created a script that demonstrates, in a simple manner, how to fix spelling errors in a given text. It accomplishes this by generating potential corrections for each misspelled word and selecting the most probable correction based on word frequencies. The code then tokenizes the input text into words, corrects each word, and ultimately displays the corrected text.

### Stemming
Stemming is a text processing technique used in natural language processing (NLP) and information retrieval to reduce words to their word stems or root forms.
For example, in English, the word "jumping" can be stemmed to "jump," and "jumps" can also be stemmed to "jump." 
This allows a search engine or text analysis tool to treat all these forms of the word as instances of the same base word, making it easier to find relevant documents or analyze 
text for patterns.
To show some algorithm we have used:
- <b>The Porter stemming algorithm</b>, also known as the Porter stemmer, is one of the most well-known and widely used stemming algorithms for the English language. 
It was developed by Martin Porter in 1980 and is a heuristic-based algorithm designed 
to reduce words to their root or stem forms by applying a series of rules and transformations.
This algorithm The Porter is available in the Natural Language Toolkit (NLTK),

- <b>The Lancaster Stemmer algorithm</b>, it's more aggressive in its stemming approach, often resulting in shorter stems that may be less recognizable as English words, while the PorterStemmer is less aggressive and generally produces longer stems that are often recognizable.

- <b>The Regexp Stemmer algorithm</b>, allows you to specify custom regular expression patterns to define how words should be stemmed. This means you have more flexibility in how words are reduced to their base or root form.

- <b>The Snowball Stemmer</b>, also known as the Porter2 Stemmer, is a stemming algorithm developed by Martin Porter and is an improvement over the original Porter Stemmer. 
Like the Porter Stemmer, the Snowball Stemmer is used to reduce words to their base or root form, particularly in the English language. 
It's designed to be more accurate and efficient than the original Porter Stemmer while still being relatively simple and effective.

[Back to top](#)

[return to readme](../readme.md)