import spacy
from spacy.cli import download as spacy_download

def download_model(model_name):
    try:
        spacy.load(model_name)
    except OSError:
        spacy_download(model_name)
