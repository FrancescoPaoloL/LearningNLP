## [Core NLP Tasks]

[return to readme](../readme.md)

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

[Back to top](#)

[return to readme](../readme.md)