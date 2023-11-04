from sklearn.metrics import accuracy_score, classification_report

# just some examples
def evaluate_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)

    return accuracy, report
