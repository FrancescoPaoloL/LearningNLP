from nltk_utils import shallow_parse, print_tree

if __name__ == "__main__":
    sentence = input()

    parsed_tree = shallow_parse(sentence, "src/ShallowParsing/grammar_config.yaml")
    print_tree(parsed_tree)
