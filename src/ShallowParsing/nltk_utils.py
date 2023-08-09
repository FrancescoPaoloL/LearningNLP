import nltk
import yaml

def download_nltk_package(package_name):
    # Check if the package is already present
    try:
        nltk.data.find('tokenizers/' + package_name)
    except LookupError:
        # If the package is not present, download it
        nltk.download(package_name, quiet=True)

def shallow_parse(sentence, config_file_path):
    # Download the Punkt tokenizer (required for tokenization)
    download_nltk_package('punkt')

    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Perform Part-of-Speech (POS) tagging to get the grammatical labelse
    pos_tags = nltk.pos_tag(words)
    print(f"POS tag / Grammatical Tagging\n{pos_tags}\n")

    # Read the grammar rules from the YAML file
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
        grammar_rules = config.get('grammar', '')

    # Use the RegexpParser to define shallow grammar for chunking
    parser = nltk.RegexpParser(grammar_rules)

    # Perform shallow parsing
    parsed_tree = parser.parse(pos_tags)

    return parsed_tree

def print_tree(tree):
    print("Annotated phrase")
    for subtree in tree.subtrees():
        if subtree.label() not in ['S', 'ROOT']:
            print(subtree.label(), ':', ' '.join(word for word, tag in subtree.leaves()))