# Learning NLP

## Shallow parsing
Shallow parsing, also known as chunking, is a technique in natural language processing to identify and group specific phrases (like noun phrases or verb phrases) within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, performs shallow parsing using the NLTK library, and then displays the parsed tree to show how different parts of the sentence are grouped together based on the specified grammar rules in the configuration file.

## Dependency Grammar
Dependency grammar is a linguistic method that emphasizes the connections between words in a sentence, showing how each word relates to others by depicting these relationships in a tree-like structure. It helps us grasp how words work together to convey meaning within a sentence.
In order to show how it works, I've made a script that takes an English sentence as input, loads a language model, creates a visual representation of how words in the sentence relate to each other (the dependency tree), and displays this tree as an image.

## Costituency Grammar
Constituency grammar is a linguistic approach that helps us understand how sentences are structured by identifying the different parts and phrases that make them up, allowing for a deeper analysis of their organization and meaning.
In order to show how it works, I've made a script that takes an English sentence as input, processes it with NLP techniques such as tokenization, POS tagging, and constituency parsing using the stanza library, and then displays the syntactic structure of the input sentence using constituency parsing.

## Text Corpora using
This Python project demonstrates a very simple text corpus analysis using the Natural Language Toolkit (NLTK) library. To achieve this, we've implemented basic functionalities on downloading essential NLTK resources, extracting the first 20 words from Blake's poems in the Gutenberg corpus, tokenizing the text, performing Part-of-Speech (POS) tagging, and conducting named-entity chunking.
Specifically, we rely on the following NLTK components:

- <b>Tokenizers/Punkt</b>: This component is the Punkt tokenizer, a pre-trained sentence tokenizer designed to split text into individual sentences based on text patterns, such as periods, exclamation points, and question marks.
- <b>Chunkers/maxent_ne_chunker</b>: This component is responsible for Named Entity Recognition (NER), which involves identifying and categorizing named entities within the text.
- <b>Corpora/words</b>: In NLTK, this refers to a collection of words in the English language.
- <b>Pos_tag</b>: This NLTK tool is used to automatically tag words in a text with their respective parts of speech.

## Text Wrangling
Text wrangling is the process of cleaning your data to make it readable by your program. To demonstrate how it works, I have created a script that demonstrates, in a simple manner, how to fix spelling errors in a given text. It accomplishes this by generating potential corrections for each misspelled word and selecting the most probable correction based on word frequencies. The code then tokenizes the input text into words, corrects each word, and ultimately displays the corrected text."


### [WIP]


## Languages and Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
<p align="left"> 
<a href="https://www.nltk.org/" target="_blank" rel="noreferrer"> <img src="./src/img/python_nltk.png" alt="python" width="50" height="50"/> </a> 
<a href="https://pyyaml.org/" target="_blank" rel="noreferrer"> <img src="./src/img/pyyaml.png" alt="python" width="110" height="50"/> </a> 
</p>

## Requirements
```
CairoSVG==2.5.2
nltk==3.6.3
Pillow==10.0.1
PyYAML==6.0.1
spacy==3.3.0
stanza==1.5.0
wip
```

## Test Coverage
todo


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



