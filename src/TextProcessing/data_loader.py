from sklearn.datasets import fetch_20newsgroups

# Define a function called `load_20newsgroups_data` that loads 
# the 20 Newsgroups dataset from scikit-learn and returns the 
# text content of the newsgroup documents and their corresponding 
# category labels. 
def load_20newsgroups_data():
    newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
    return newsgroups.data, newsgroups.targeta

