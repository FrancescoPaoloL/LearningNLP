'''
The bag of words represents each text document as a numeric vector, 
where each dimension corresponds to a specific word from the corpus, 
and the value represents its frequency in the document (usually 0 or 1).

In simple terms, this code takes a collection of text documents (the corpus) and 
counts how many times each unique word appears in each document.

The feature matrix is traditionally represented as a sparse matrix (not dense matrix) because 
it avoids allocating memory for all possible entries, especially zeros. 
This efficient representation saves a significant amount of memory, which becomes crucial when 
working with extensive text datasets and larger vocabularies.

Each column/dimension represents a word from the corpus.
Each row represents one of our document.
The value of any cell repreents the number of times that word occurs in the specidic document.

Let's take an example: 

   bacon  beans  beautiful  blue  breakfast  brown  dog  eggs  fox  green  ham  jumps  kings  lazy  love  quick  sausages  sky  toast  today
0      0      0          1     1          0      0    0     0    0      0    0      0      0     0     0      0         0    1      0      0
1      0      0          1     1          0      0    0     0    0      0    0      0      0     0     1      0         0    1      0      0
2      0      0          0     0          0      1    1     0    1      0    0      1      0     1     0      1         0    0      0      0

3      1      1          0     0          1      0    0     1    0      0    1      0      1     0     0      0         1    0      1      0   <---

4      1      0          0     0          0      0    0     1    0      1    1      0      0     0     1      0         1    0      0      0
5      0      0          0     1          0      1    1     0    1      0    0      0      0     1     0      1         0    0      0      0
6      0      0          1     1          0      0    0     0    0      0    0      0      0     0     0      0         0    2      0      1
7      0      0          0     0          0      1    1     0    1      0    0      0      0     1     0      1         0    0      0      0

In row 3 (document 3), there is a 1 in the "bacon" column and a 1 in the "eggs" column. 
This indicates that document 3 contains the word "bacon" once and the word "eggs" once

'''

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def get_bag_of_words(corpus):
    cv = CountVectorizer(min_df=0., max_df=1.)
    cv_matrix = cv.fit_transform(corpus)
    cv_matrix = cv_matrix.toarray()
    vocab = cv.get_feature_names()
    bag_of_words_df = pd.DataFrame(cv_matrix, columns=vocab)
    
    return bag_of_words_df
