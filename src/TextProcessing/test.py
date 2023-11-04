import data_loader
import text_normalization
import feature_extraction
import text_classifier
import evaluate
from sklearn.model_selection import train_test_split
from tabulate import tabulate

def test_model(model):
    # Load testing data, normalization it
    # and make Feature extraction for testing data
    test_documents, test_classes = data_loader.load_20newsgroups_data()
    normalized_test_documents = text_normalization.normalize_text(test_documents)
    X_test_features = feature_extraction.extract_features(normalized_test_documents)

    # Print some information
    print("Testing with model")
    print("Model classes:", model.classes_)
    print("Number of features:", X_test_features.shape[1])

    # Make predictions on the test set using the provided model...
    predictions = text_classifier.predict(model, X_test_features)

    # ... and evaluate the model's performance on the test set
    accuracy, report = evaluate.evaluate_model(test_classes, predictions)

    # Print evaluation results
    print("Model evaluation:")
    print("Accuracy:", accuracy)

    # Display classification report as a table
    headers = ["Class", "Precision", "Recall", "F1-Score", "Support"]
    table_data = []
    for class_name, metrics in report.items():
        if class_name.isnumeric():
            row = [class_name, metrics['precision'], metrics['recall'], metrics['f1-score'], metrics['support']]
            table_data.append(row)

    print("Classification Report:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

