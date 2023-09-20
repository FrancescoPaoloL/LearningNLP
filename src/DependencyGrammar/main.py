from dependency_tree import draw_dependency_tree

if __name__ == "__main__":
    print("Please insert a phrase. I suggest a default example but you can write anything you want.")
    default_input = "The brown fox is quick and he is jumping over the lazy dog"
    input_sentence = input(f"Example: {default_input}. ")
    input_sentence = input_sentence.strip() or default_input
    draw_dependency_tree(input_sentence)
