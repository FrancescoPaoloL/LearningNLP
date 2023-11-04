from sklearn.naive_bayes import MultinomialNB

# we use MultinomialNB

def build_naive_bayes_model(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    return model.predict(X_test)

