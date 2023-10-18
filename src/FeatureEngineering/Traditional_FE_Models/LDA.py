from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def lda_topic_modeling(corpus, labels, n_topics=3, max_features=1000):
    cv = CountVectorizer(max_features=max_features, stop_words='english')
    cv_matrix = cv.fit_transform(corpus)

    lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    dt_matrix = lda.fit_transform(cv_matrix)

    topic_columns = [f'Topic_{i + 1}' for i in range(n_topics)]
    features = pd.DataFrame(dt_matrix, columns=topic_columns)

    return features