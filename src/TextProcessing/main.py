import data_loader
import text_normalization
import feature_extraction
import text_classifier
import test

# Load data
documents, classes = data_loader.load_20newsgroups_data()

# Make text normalization and feature extraction
normalized_documents = text_normalization.normalize_text(documents)

X_train_features = feature_extraction.extract_features(normalized_documents)

# Build and train the model
model = text_classifier.build_naive_bayes_model(X_train_features, classes)

print("Model training completed.")
print("Model classes:", model.classes_)
print("Number of features:", X_train_features.shape[1])

# testing the model
test.test_model(model)  # Pass the model to the testing function
