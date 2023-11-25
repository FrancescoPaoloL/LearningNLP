from distance_metrics import manhattan_distance, euclidean_distance, cosine_distance

document1 = [3, 1, 2]
document2 = [1, 2, 0]

manhattan_dist = manhattan_distance(document1, document2)
euclidean_dist = euclidean_distance(document1, document2)
cosine_dist = cosine_distance(document1, document2)

print("Document 1:", document1)
print("Document 2:", document2)
print("\nManhattan Distance:", manhattan_dist)
print("Euclidean Distance:", euclidean_dist)
print("Cosine Distance:", cosine_dist)

