# Learning NLP
The topics of this repository have been taken from the excellent book 'Text Analytics with Python' by Dipanjan Sarkar although the examples and code are mostly completely different.

## Index
1. **Syntax Analysis**
   - [Shallow Parsing](#shallow-parsing)
   - [Dependency Grammar](#dependency-grammar)
   - [Constituency Grammar](#constituency-grammar)
2. **Text Preprocessing**
   - [Text Wrangling](#text-wrangling)
     - [Stemming](#stemming)
   - [Text Corpora](#text-corpora-using)
3. **Feature Engineering**
   - [Feature Engineering](#feature-enginering)
4. **Core NLP Tasks**
   - [Text Processing](#text-processing)
   - [Text Summarization](#text-summarization)
   - [Text Similarity](#text-similarity)
5. **Information Retrieval**
   - [Okapi BM25 Ranking Formula](#okapi-bm25-ranking-formula)
6. **Unsupervised Learning**
   - [Document Clustering](#document-clustering)
7. **Advanced Applications**
   - [Semantic Analysis](#semantic-analysis)
   - [Sentiment Analysis](#sentiment-analysis)

## Syntax Analysis
### Shallow parsing
Shallow parsing, also known as chunking, is a technique in natural language processing to identify and group specific phrases (like noun phrases or verb phrases) within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, performs shallow parsing using the NLTK library, and then displays the parsed tree to show how different parts of the sentence are grouped together based on the specified grammar rules in the configuration file.

### Dependency Grammar
Dependency grammar is a linguistic method that emphasizes the connections between words in a sentence, showing how each word relates to others by depicting these relationships in a tree-like structure. It helps us grasp how words work together to convey meaning within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, loads a language model, creates a visual representation of how words in the sentence relate to each other (the dependency tree), and displays this tree as an image.

### Costituency Grammar
Constituency grammar is a linguistic approach that helps us understand how sentences are structured by identifying the different parts and phrases that make them up, allowing for a deeper analysis of their organization and meaning.
In order to show how it works, I've made a script that takes an English sentence as input, processes it with NLP techniques such as tokenization, POS tagging, and constituency parsing using the stanza library, and then displays the syntactic structure of the input sentence using constituency parsing.

## [Text Preprocessing](#index)
### Text Corpora using
This Python project demonstrates a very simple text corpus analysis using the Natural Language Toolkit (NLTK) library. To achieve this, we've implemented basic functionalities on downloading essential NLTK resources, extracting the first 20 words from Blake's poems in the Gutenberg corpus, tokenizing the text, performing Part-of-Speech (POS) tagging, and conducting named-entity chunking.
Specifically, we rely on the following NLTK components:

- <b>Tokenizers/Punkt</b>: This component is the Punkt tokenizer, a pre-trained sentence tokenizer designed to split text into individual sentences based on text patterns, such as periods, exclamation points, and question marks.
- <b>Chunkers/maxent_ne_chunker</b>: This component is responsible for Named Entity Recognition (NER), which involves identifying and categorizing named entities within the text.
- <b>Corpora/words</b>: In NLTK, this refers to a collection of words in the English language.
- <b>Pos_tag</b>: This NLTK tool is used to automatically tag words in a text with their respective parts of speech.

## [Text Wrangling](#index)
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


## [Feature enginering](#index)
Feature engineering in NLP involves the process of transforming and creating meaningful features from raw text data to improve the performance of machine learning models. This is essential because many machine learning algorithms require numerical input data, while NLP tasks often involve working with unstructured text data. 
Typically this process includes the following key steps:
- <b>Text Preprocessing</b>: This step involves cleaning and preparing the raw text data.
- <b>Feature Extraction</b>: In NLP, feature extraction involves converting text data into numerical features that can be used by machine learning algorithms. Common techniques for feature extraction include:</b>
    - <b><i>TRADITIONAL FEATURES ENGINEERING MODELS</i></b>
        - <b><i>Bag of Words (BoW)</i></b>: Representing text as a matrix of word frequencies or presence/absence indicators.
        - <b><i>N-grams</i></b>: Capturing sequences of N words to consider local context.
        - <b><i>Term Frequency-Inverse Document Frequency (TF-IDF)</i></b>: Assigning weights to words based on their importance in a document relative to a corpus of documents.
            - We even have a specific example when we use TF-IDF vectorization.
        - <b><i>Documents Similarity</i></b>: document distance in NLP refers to quantifying how similar or dissimilar two or more text documents are. A very common metrics include cosine similarity, so I've done a script which calculates and compares cosine similarity between three pairs of matrices. It does this using both a library version and a custom "from scratch" version of the cosine similarity calculation function. 
        - <b><i>Document Clustering</i></b>: document clustering is a text analysis technique that groups similar documents together based on their content. This process makes it easier to identify patterns and themes within a large set of documents. To illustrate how this works, I've created a script that performs hierarchical clustering on a collection of documents. It begins by measuring the similarity between the documents using their TF-IDF representations. Then, it constructs a hierarchical tree structure (dendrogram) to visualize how the documents are grouped based on their similarity. For the sake of simplicity, I've used only four sentences as documents.
        - <b><i>Topic Models</i></b>: they are statistical models used to discover hidden thematic structures within a collection of documents. They enable the identification and analysis of common topics or themes. As an example, I've chosen the Latent Dirichlet Allocation (LDA) algorithm and implemented a script that performs topic modeling on the text data. This script returns a Pandas DataFrame containing the topic distribution for each document in the corpus.
    - <b><i>ADVANCED FEATURES ENGINEERING MODELS</i></b>
        - <b><i>Word2vec</i></b>: This technique transforms words into numerical vectors, enabling computers to comprehend and process them effectively; it is an integral part of the vector space model, representing words as vectors in a manner where similar words are positioned close in this space, in order to make the original text undestable by the computer. To show how this works I've create a script that uses the Gensim library to train a Word2Vec model on a given corpus of text; then finding the vector representation of the word 'sun' (for example) and identifying the top 3 words most similar to 'sun' based on the learned word embeddings.
        - <b><i>CBOW (Continuous Bag of Words)</i></b>: it is a word embedding model that learns to predict a word from its context words in a sentence, creating word vectors that represent words' meanings and relationships. To provide a simple example, I've developed a script that tokenizes and preprocesses Shakespeare's "Hamlet," generates training data for a Skip-Gram embedding model, trains the model, subsequently extracts word embeddings to predict the context words given a target word.
        - <b><i>Skip-Gram</i></b>: it is a technique that helps us grasp the meanings of words and their relationships by analyzing the context in which they appear within a substantial body of text. In simpler terms, it enables us to capture the semantic connections between words. To illustrate, I've developed a script that performs tasks akin to the CBOW example. However, in this case, it extracts word embeddings to predict the target word based on its context words.
        - <b><i>Gensim</i></b>: it is a efficent implementation of the Word2Vec model. It's widely used for tasks like text document similarity, topic extraction, and word vector representations. To illustrate, I've developed a script that training a Gensim Word2Vec model on a text corpus, extracting word embeddings, and finding similar words to a specified target word, with adjustable model parameters.
        - <b><i>Glove</i></b>: it stands for 'Global Vectors' and is an unsupervised learning model that can be used to obtain dense word vectors, similar to Word2Vec. To illustrate how it works, I've created a script that processes text, generating word embeddings using both CBOW and GloVe. CBOW captures word meanings based on local context, while GloVe analyzes word relationships in a broader context. Finally, the script performs word similarity and analogy tasks, such as measuring the similarity between 'king,' 'queen,' and 'woman,' if these words are present in the model's vocabulary.
    In the 'FeatureEngineering' directory, you can find simple examples of how to use these techniques.


## [Core NLP Tasks](#index)
### Text Processing
Text processing in NLP involves preparing and analyzing text data with these key steps:
    - Gather text data.
    - Break text into smaller units (tokenization).
    - Clean the text by removing noise.
    - Remove common words (stopwords).
    - Reduce words to their base form (lemmatization or stemming).
    - Standardize text (normalization).
    - Convert text to features for analysis.
    - Perform NLP tasks like classification or sentiment analysis.
    - Post-process results as needed.
    - Evaluate model performance if using machine learning.
In this case I've developed a simple example that demonstrates all the necessary steps for proper execution.

### Text Summarization
Text Summarization in NLP automates the extraction of crucial information from a document, condensing it for brevity. To demonstrate its functionality, we have created:

- A simple demonstration illustrating how to calculate Eigenvalues and Eigenvectors, visualized as arrows. The first eigenvector is represented in red, and the second in blue.
- A script for extractive text summarization using the Singular Value Decomposition (SVD) technique. This script tokenizes and preprocesses input text, computes the TF-IDF matrix, applies SVD to capture document structure, and selects key sentences based on the first component of the decomposition.

To extract information, we employ "Keyphrase Extraction" with two major techniques:

- **Collocations:** This involves identifying phrases where words tend to occur together more often than expected by chance. A script demonstrates this by identifying and displaying collocations based on their frequency and statistical significance using the Pointwise Mutual Information (PMI) metric.

- **Score Weight:** Weighted tag-based phrase extraction assigns weights to linguistic tags and calculates a combined weight for phrases based on the tags of their constituent words. The general idea is to use weights associated with each tag to score and rank phrases. Refer to the script for details.

**Topic Modeling** focuses on extracting themes/concepts from a corpora, utilizing two main methods:

- **Latent Semantic Indexing (LSI):** This technique analyzes relationships between words in a set of documents to uncover hidden semantic structures. A script creates an LSI model and prints the topics. The output is interpreted as weights indicating the importance of each word in a topic. An example LSI representation of a new document is provided for interpretation.

- **Latent Dirichlet Allocation (LDA):** This technique discovers topics and their distribution across documents. The script preprocesses research papers, builds an LDA model using Gensim, and prints the generated topics and LDA representation of a sample document. The information shared earlier regarding LSI output applies similarly to this script.

### Text Similarity
Text similarity is a measure of how closely related or alike two pieces of text are in terms of content, structure, or meaning. To illustrate this, a simple example introduces various distance measurements in the context of text analysis, using only logic written from scratch, without any external libraries.
Then I've made a script which demonstrate how Okapi BM25 (BM is an abbreviation of best matching) works.
First of all, it is a ranking function used to rank a collection of documents based on their relevance to a given query. 


## [Information Retrieval](#index)
### Okapi BM25 Ranking Formula
The Okapi BM25 ranking formula is used to score the relevance of a document to a given search query. It is commonly employed in information retrieval systems.
It is defined as:

$$ \text{BM25}(D, Q) = \sum_{i=1}^{n} \frac{{f(q_i, D) \cdot (k_1 + 1)}}{{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{{\text{dl}(D)}}{{\text{avgdl}}}\right)}} \cdot \log\left(\frac{{N - n(q_i) + 0.5}}{{n(q_i) + 0.5}}\right) \cdot \frac{{(k_2 + 1) \cdot qf(q_i, Q)}}{{k_2 + qf(q_i, Q)}} $$
 
This formula calculates a score representing the relevance of the document to the query, taking into account the frequency of query terms in the document and their overall distribution in the document collection.
The script make output that represents the BM25 scores for each document in the provided collection based on the given query, "quick brown fox." 
For example we get:

    Document 1: "The quick brown fox jumps over the lazy dog."
        BM25 Score: 1.3076713878207966

    Document 2: "A quick brown dog outpaces a lazy fox."
        BM25 Score: 0.9219687396718056

    Document 3: "The lazy dog sleeps all day."
        BM25 Score: 0.0

As you can see, Document 1 contains all the terms from the query ("quick," "brown," and "fox"), so it has the higher score. On the opposite, Document 3 has a BM25 score of 0.0 because it doesn't contain any of the terms from the query. 

## [Unsupervised Learning](#index)
### Document Clustering
Through this technique documents are grouped into clusters based on their content similarity; the objective is to discover inherent structures without predefined categories or labels.
There are some method to do that. One popular is:<br>
    - <b><i>K-means clustering</i></b>: it is a unsupervised machine learning algorithm used for partitioning a dataset into 'k' distinct subgroups or clusters. The algorithm iteratively assigns data points to clusters based on their similarity to the cluster centroids and updates the centroids to minimize the total within-cluster variance. In order to show you how it works I've made a script that uses this algorithm from scratch.<br>
    - <b><i>Affinity Propagation</i></b>: Affinity Propagation is a clustering algorithm designed to identify representative points within a dataset. Unlike traditional clustering methods where the number of clusters needs to be specified beforehand, Affinity Propagation determines both the number of clusters and the exemplars simultaneously. Simply put, the algorithm iteratively exchanges messages between data points to find a set of exemplars that maximize a combination of similarity and preference values. The data points are then assigned to the nearest exemplar, forming clusters. To illustrate how it works, I've created a script utilizing this algorithm, and the results are visualized for clarity.

## [Advanced Applications](#index)
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
### 

## Languages and Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
<p align="left"> 
<a href="https://www.nltk.org/" target="_blank" rel="noreferrer"> <img src="./src/img/python_nltk.png" alt="python" width="50" height="50"/> </a> 
<a href="https://pyyaml.org/" target="_blank" rel="noreferrer"> <img src="./src/img/pyyaml.png" alt="python" width="110" height="50"/> </a> 
</p>

## Requirements
```
CairoSVG==2.7.1
gensim==4.3.2
keras==3.0.2
matplotlib==3.6.3
nltk==3.8
numpy==1.24.2
pandas==2.1.4
Pattern==3.6
Pillow==10.1.0
PyYAML==6.0.1
scikit_learn==1.3.2
scipy==1.11.4
spacy==3.7.2
stanza==1.7.0
tabulate==0.9.0
textblob==0.17.1
vaderSentiment==3.3.2
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



