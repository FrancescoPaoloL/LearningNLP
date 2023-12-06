from nltk.tree import Tree

def print_named_entity_tree(tree):
    for subtree in tree:
        if isinstance(subtree, Tree):
            print_named_entity_tree(subtree)
        else:
            print(subtree, end=' ')

