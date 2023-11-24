from nltk.tokenize import word_tokenize
from itertools import combinations
from pos_weight_calculator import calculate_weight

def calculate_combination_weights(text):
    tokens = word_tokenize(text)
    token_combinations = []

    for r in range(1, len(tokens) + 1):
        token_combinations.extend(combinations(tokens, r))

    combination_weights = {}
    for combo in token_combinations:
        weight = calculate_weight(combo)
        combination_weights[combo] = weight

    return combination_weights

