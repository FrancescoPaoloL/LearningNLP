## [Advanced Applications] 

[return to readme](../readme.md)

### Semantic Analysis
Semantic analysis helps us understand the meaning of words, sentences, and texts. We can use a tool called WordNet to organize English words into groups of similar meanings called Synsets. It shows how words are connected.
There are various ways to represent semantic associated with statements and propositions; the main are:
- <b><i>Lexical Semantic Relations</i></b>: it's about understanding how words are connected in meaning or how they relate to each other. So I've made a script that extracts synonyms from WordNet, and displaying the synonyms if present.
- <b><i>Named Entity Recognition (NER)</i></b>: identifies and classifies specific entities (like names of people, places, organizations) in a text; for example: it recognizes "John" as a person, "New York" as a location, or "Apple" as a company in a sentence. In order to do that, we've made a simple example that reads a text file, tokenizes it, performs part-of-speech tagging, and applies Named Entity Recognition using the NLTK library. In this case the output is: "('Rizz', 'NNP') ('is', 'VBZ') ('an', 'DT') ... " and so on and it should read: 'Rizz' is 'NNP' (this tuple indicates that the word "Rizz" is recognized as a proper noun (NNP), which is often used for names of people, places, etc.). You can see this: 
    - (',', ','): this tuple indicates that the comma ',' in the text has been recognized, and its part-of-speech (POS) tag is also a comma (in fact, in POS tagging, punctuation marks are often assigned the same POS tag as the punctuation itself.
    - ('``', '``'): in this case, the tuple indicates the presence of an opening quotation mark (''). The POS tag '' is often used to represent opening or left double quotation marks in text.
- <b><i>Semantic Representations</i></b>: turning the meaning of words into a language computers can use to understand and work with; for example it represents the meaning of "happy" as a positive emotion in a format a computer can process. To show how it works I0ve made a very simple script that defines logical predicates related to hunger and eating preferences for different individuals ('she', 'he', 'they') and tests these predicates for each person according to the specified logical conditions.
- <b><i>WordNet Synsets</i></b>: it organizes words into sets (synsets) based on their meanings and relationships; for example, it groups words like "car" and "automobile" into a synset because they have a similar meaning. To show how it works I've created a simple example using WordNet through NLTK. It finds and prints words with similar meanings (synonyms) and more general words (hypernyms) for a chosen word. In simpler terms, a Synset is like a category for words that are related in meaning. To make it clearer, I've made a script that takes a word, like "bat," and shows all the possible categories it could belong to using WordNet.
- <b><i>Word Sense Disambiguation</i></b>: it resolves ambiguity when a word has multiple meanings by determining the correct sense in a particular context; a classical example can be figuring out whether "bank" refers to a financial institution or the side of a river in a sentence.

### Sentiment Analysis
Simply put, Sentiment Analysis is the task of identifying the emotional tone or 'sentiment' conveyed in a piece of text, whether it is positive, negative, or neutral. This process can involve Supervised Learning-based models that learn from labeled data, while unsupervised lexicon-based models (a lexicon is just a predefined dictionary) utilize predefined dictionaries for sentiment analysis. Lexicons such as AFINN, BingLiu, MPQA, Pattern, SentiWordNet, TextBlob, and VADER employ varied strategies to extract sentiment information from text. To illustrate, we've created an example for each of these. So let's take a look at these kinds of lexicons and their corresponding explanation scripts:
- <b><i>AFINN Lexicon:</i></b> A sentiment analysis tool assigning scores to words for straightforward emotion assessment in text. The associated script is straightforward: input a text for analysis, and it returns the sentiment.
- <b><i>BingLiu Lexicon:</i></b> A tool that assesses words in text to determine whether they convey happiness or sadness. The relative script using this lexicon and produce an output like this:
    Sentence: Great example using Lexicon Python
    Sentiment Scores: ['positive', 'unknown', 'unknown', 'unknown', 'unknown']
that means: the word "great" is present in the lexicon with a positive sentiment, so its score is "positive"; "example" is not present in the lexicon so "unknown" and so on.
- <b><i>MPQA Lexicon:</i></b> A list of words indicating whether they convey positive or negative sentiments in text. The associated script takes a text as input for analysis, and it returns the sentiment.
- <b><i>Pattern Lexicon:</i></b> Analyzes specific word patterns to discern emotions in textual content. So the example code uses the pattern.en library to perform sentiment analysis analyzing sentiment to extract polarity and subjectivity scores. We remind you that in sentiment analysis:
    - Polarity: indicates the emotional tone (positive, negative, or neutral) of a text.
    - Subjectivity: measures how subjective or objective the text is (opinionated vs. factual).
- <b><i>SentiWordNet Lexicon:</i></b> A list assigning scores to words, facilitating the nuanced understanding of emotions in text. The example calculates sentiment scores for a given sentence assigning sentiment scores based on SentiWordNet's sentiment synsets.
- <b><i>TextBlob Lexicon:</i></b> A tool that examines words to determine the overall positive or negative tone of text. The example simply uses this tool.
- <b><i>VADER Lexicon:</i></b> A tool specialized in comprehending sentiments in text, particularly on social media platforms. The example simply uses this tool.

[Back to top](#)

[return to readme](../readme.md)
