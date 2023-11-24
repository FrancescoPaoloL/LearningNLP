import os
import tarfile
from io import BytesIO
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing import strip_punctuation, strip_numeric

def preprocess_documents(tgz_path):
    with open(tgz_path, 'rb') as file:
        compressed_file_content = BytesIO(file.read())

    with tarfile.open(fileobj=compressed_file_content, mode='r:gz') as tar:
        papers_content = []
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

    preprocessed_documents = [
        strip_numeric(strip_punctuation(remove_stopwords(doc))).split()
        for doc in papers_content
    ]

    return preprocessed_documents

