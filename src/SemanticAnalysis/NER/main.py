from named_entity_recognition import named_entity_recognition
from tree_printer import print_named_entity_tree

# Read the content of the document
document_path = "Rizz_Wikipedia_Document.txt"

with open(document_path, 'r', encoding='utf-8') as file:
    document_content = file.read()

# Perform Named Entity Recognition on the document content
result = named_entity_recognition(document_content)

# Print the result in a readable format
print_named_entity_tree(result)

