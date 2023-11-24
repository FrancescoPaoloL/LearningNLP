from token_combination_calculator import calculate_combination_weights

def main():
    text = "Great acting and compelling story"
    
    combination_weights = calculate_combination_weights(text)

    max_combination = max(combination_weights, key=combination_weights.get)
    max_weight = combination_weights[max_combination]

    print("Text:", text)
    print("Token Combinations and Weights:")
    for combo, weight in combination_weights.items():
        print(f"{combo}: {weight}")

    print("\nMax Weight Combination:")
    print(f"{max_combination}: {max_weight}")

if __name__ == "__main__":
    main()

