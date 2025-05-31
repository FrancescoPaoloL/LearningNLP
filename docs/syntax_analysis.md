## Syntax Analysis

[return to readme](../readme.md)

### Shallow parsing
Shallow parsing, also known as chunking, is a technique in natural language processing to identify and group specific phrases (like noun phrases or verb phrases) within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, performs shallow parsing using the NLTK library, and then displays the parsed tree to show how different parts of the sentence are grouped together based on the specified grammar rules in the configuration file.

### Dependency Grammar
Dependency grammar is a linguistic method that emphasizes the connections between words in a sentence, showing how each word relates to others by depicting these relationships in a tree-like structure. It helps us grasp how words work together to convey meaning within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, loads a language model, creates a visual representation of how words in the sentence relate to each other (the dependency tree), and displays this tree as an image.

### Costituency Grammar
Constituency grammar is a linguistic approach that helps us understand how sentences are structured by identifying the different parts and phrases that make them up, allowing for a deeper analysis of their organization and meaning.
In order to show how it works, I've made a script that takes an English sentence as input, processes it with NLP techniques such as tokenization, POS tagging, and constituency parsing using the stanza library, and then displays the syntactic structure of the input sentence using constituency parsing.


### Stemming
## [Text Preprocessing]
### Text Corpora using
This Python project demonstrates a very simple text corpus analysis using the Natural Language Toolkit (NLTK) library. To achieve this, we've implemented basic functionalities on downloading essential NLTK resources, extracting the first 20 words from Blake's poems in the Gutenberg corpus, tokenizing the text, performing Part-of-Speech (POS) tagging, and conducting named-entity chunking.
Specifically, we rely on the following NLTK components:

- <b>Tokenizers/Punkt</b>: This component is the Punkt tokenizer, a pre-trained sentence tokenizer designed to split text into individual sentences based on text patterns, such as periods, exclamation points, and question marks.
- <b>Chunkers/maxent_ne_chunker</b>: This component is responsible for Named Entity Recognition (NER), which involves identifying and categorizing named entities within the text.
- <b>Corpora/words</b>: In NLTK, this refers to a collection of words in the English language.
- <b>Pos_tag</b>: This NLTK tool is used to automatically tag words in a text with their respective parts of speech.

[Back to top](#)

[return to readme](../readme.md)