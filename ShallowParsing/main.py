from nltk_utils import shallow_parse, print_tree

if __name__ == "__main__":
    # "With these updates to the grammar, the script should now provide a more accurate and non-repetitive output for the identified groups in the input sentence."
    sentence = input()

    parsed_tree = shallow_parse(sentence, "grammar_config.yaml")
    print_tree(parsed_tree)
