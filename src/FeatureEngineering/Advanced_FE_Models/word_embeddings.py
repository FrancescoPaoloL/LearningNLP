import numpy as np
from keras.models import Sequential
from keras.layers import Embedding, Dense, Lambda

def generate_cbow_data(corpus, tokenizer, window_size=2):
    # we've chosen window_size = 1 as default
    # because, for sake of simplicity, it considers only 
    # the immediately adjacent words on either side of 
    # the target word as context words. 
    X = [] # here will be stored the context words
    Y = [] # here will be stored the target words
    for i, target_word in enumerate(corpus):
        context_words = []
        # This prevents "start" from being a negative value 
        start = max(0, i - window_size)
        # This ensures that "stop" doesn't exceed the length of the text
        stop = min(i + window_size + 1, len(corpus))
        for j in range(start, stop):
            if i != j:
                # it means the word at position 'j' 
                # in the 'corpus' is a context word.
                context_words.append(corpus[j])
        for context_word in context_words:
            X.append(tokenizer.word_index[context_word])
            Y.append(tokenizer.word_index[target_word])

    return np.array(X), np.array(Y)

def train_model(X, Y, word_index):
    # Older papers in NLP used 300 conventionally
    # https://petuum.medium.com/embeddings-a-matrix-of-meaning-4de877c9aa27. 
    # More recent papers used 512, 768, 1024.
    embedding_dim = 300

    # We use a a Sequential model beacuse is appropriate 
    # for a plain stack of layers where each layer has exactly 
    # one input tensor and one output tensor.
    model = Sequential()

    # we convert words into numerical vectors...
    model.add(Embedding(input_dim=len(word_index) + 1, output_dim=embedding_dim, input_length=1))

    # this line adds a layer to your model that takes an input and returns 
    # the first value of that input as a vector (via Lambda function)
    model.add(Lambda(lambda x: x[0], output_shape=(embedding_dim)))

    # This adds a layer that produces a probability distribution via softmax algorithm
    model.add(Dense(units=embedding_dim, activation='softmax'))

    # we use the "mean squared error," which means it calculates the average of 
    # the squared differences between predictions and correct values via Adams optimizer
    model.compile(loss='mean_squared_error', optimizer='adam')
    print(model.summary())

    model.fit(X, Y, epochs=10, batch_size=32)

    return model

def get_word_embeddings(model):
    # In the model we have three layers:
    #   - Embedding Layer aka model.layers[0]
    #   - Lambda Layer aka model.layers[1]
    #   - Dense Layer ak model.layers[2]
    word_embeddings = model.layers[0].get_weights()[0]
    return word_embeddings