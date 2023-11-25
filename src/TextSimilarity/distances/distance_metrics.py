import math

def manhattan_distance(vector1, vector2):
    return sum(abs(x - y) for x, y in zip(vector1, vector2))

def euclidean_distance(vector1, vector2):
    return math.sqrt(sum((x - y)**2 for x, y in zip(vector1, vector2)))

def cosine_similarity(vector1, vector2):
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x**2 for x in vector1))
    magnitude2 = math.sqrt(sum(y**2 for y in vector2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # because it avoids division by zero

    return dot_product / (magnitude1 * magnitude2)

def cosine_distance(vector1, vector2):
    return 1 - cosine_similarity(vector1, vector2)

