"""
We need a text ccorpus to work on and demostrate different feature engineering an representation methodologies.
To keep thing simple, we bult a short and simple text corpus.

This code loads and preprocesses some text data, then creates three different models 
to represent the text: Bag of Words, Bag of N-Grams, and TF-IDF, and finally, it 
prints the results of each model.

"""

from menuDef import *

def main():
    # Define 'corpus' and its associated labels
    corpus = [  
                "The sun sets over the horizon, painting the sky with colors.",
                "Surfers ride the waves as dolphins swim nearby.",
                "In the depths of the forest, birds chirp and leaves rustle.",
                "Gourmet chefs prepare exquisite dishes with precision and creativity.",
                "Children play in the park, laughing and enjoying the sunshine.",
                "The city streets are bustling with people, cars, and music.",
                "A lone hiker explores the rugged mountain terrain.",
                "Artists express their emotions through paintings and sculptures."
            ]

    labels = ["nature", "nature", "nature", "food", "family", "city", "adventure", "art"]

    matrices = [
                {
                    "name": "\nSimilar Matrices",
                    "matrix1": np.array([[1, 1, 1],
                                        [1, 1, 1],
                                        [1, 1, 1]]),
                    "matrix2": np.array([[1, 1, 1],
                                        [1, 1, 1],
                                        [1, 1, 1]])
                },
                {
                    "name": "\nNot Similar Matrices",
                    "matrix1": np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]),
                    "matrix2": np.array([[9, 8, 7],
                                        [6, 5, 4],
                                        [3, 2, 1]])
                },
                {
                    "name": "\nVarying Matrices",
                    "matrix1": np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]),
                    "matrix2": np.array([[2, 3, 4],
                                        [5, 6, 7],
                                        [8, 9, 10]])
                }
            ]
  
    while True:
        print_menu(corpus, labels, matrices)
        choice = input("Enter your choice (0-6): ")
        print(f"You've chosen {choice}\n")

        if choice == "0":
            break
        elif choice == "1":
            bags(corpus, labels)
            pass
        elif choice == "2":
            extracting_features(corpus)
            pass
        elif choice == "3":
            documents_similarity(matrices)
            pass
        elif choice == "4":
            documents_clustering(corpus[:4])
            pass
        elif choice == "5":
            LDA_algorithm(corpus, labels)
            pass
        elif choice == "6":
            word2vec_example(corpus)
            pass
        else:
            print("Invalid choice. Please select a valid option.")

    print("Bye!")

if __name__ == "__main__":
    main()