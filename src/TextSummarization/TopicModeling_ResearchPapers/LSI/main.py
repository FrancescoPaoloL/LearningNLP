import tarfile
from io import BytesIO
from preprocess import preprocess_documents
from build_model import build_lsi_model
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing import strip_punctuation, strip_numeric
from gensim import corpora
from gensim.models import LsiModel

tgz_path = '../papers/nips12raw_str602.tgz'

with open(tgz_path, 'rb') as file:
    compressed_file_content = BytesIO(file.read())

with tarfile.open(fileobj=compressed_file_content, mode='r:gz') as tar:
    papers_content = []  # List to store the content of each research paper

    total_files = len([tarinfo for tarinfo in tar if tarinfo.isfile() and tarinfo.name.endswith(".txt")])
    current_file = 0

    for tarinfo in tar:
        if tarinfo.isfile() and tarinfo.name.endswith(".txt"):
            current_file += 1
            print(f"Processing file {current_file}/{total_files}...")

            try:
                file_content = tar.extractfile(tarinfo).read().decode('utf-8')
            except UnicodeDecodeError:
                file_content = tar.extractfile(tarinfo).read().decode('latin-1', errors='ignore')
            papers_content.append(file_content)

preprocessed_documents = preprocess_documents(papers_content)

dictionary = corpora.Dictionary(preprocessed_documents)

corpus = [dictionary.doc2bow(doc) for doc in preprocessed_documents]

# Build the LSI model
num_topics = 5
lsi_model = build_lsi_model(preprocessed_documents, num_topics=num_topics)

print("\nLSI Topics:")
print(lsi_model.print_topics())

# Example: Transform a new document to LSI space
new_document_index = 0
new_bow = corpus[new_document_index]
new_lsi = lsi_model[new_bow]
print("\nLSI representation of the new document:")
print(new_lsi)

