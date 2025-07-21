import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def classify(features_path, match_column='MATCH'):
    df = pd.read_csv(features_path)
    if match_column not in df.columns:
        raise ValueError(f"{match_column} column is missing.")
    
    X = df.drop(match_column, axis=1)
    y = df[match_column]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    model = svm.SVC(kernel='linear', gamma='auto', C=1000)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    print(classification_report(y_test, y_pred))

    return model, x_train, x_test, y_train, y_test, y_pred

# Example usage:
# model, x_train, x_test, y_train, y_test, y_pred = classify('data/features_with_labels.csv')
