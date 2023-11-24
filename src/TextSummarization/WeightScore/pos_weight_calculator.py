import nltk
from nltk import pos_tag
from itertools import combinations

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def calculate_weight(tokens):
    weight_criteria = {'NN': 2.0, 'VGB': 1.5}  # Noun, Adjective
    total_weight = 0.0

    pos_tags = pos_tag(tokens)

    for i in range(len(pos_tags)):
        for j in range(i + 1, len(pos_tags) + 1):
            weight = sum(weight_criteria.get(pos[:2], 0.0) for word, pos in pos_tags[i:j])
            total_weight += weight

    return total_weight

