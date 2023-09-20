from nltk_utils import shallow_parse, print_tree

if __name__ == "__main__":
    print("Please insert a phrase. I suggest a default example but you can write anything you want.")
    default_input = "The brown fox is quick and he is jumping over the lazy dog"
    sentence = input(f"Example: {default_input}. ")
    sentence = sentence.strip() or default_input

    parsed_tree = shallow_parse(sentence, "src/ShallowParsing/grammar_config.yaml")
    print_tree(parsed_tree)
