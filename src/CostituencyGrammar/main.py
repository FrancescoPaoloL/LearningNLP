# see https://stanfordnlp.github.io/stanza/constituency.html

import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,constituency')
sentence = input()
doc = nlp(sentence)
for sentence in doc.sentences:
    print(sentence.constituency)

