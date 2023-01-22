import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def predict_victory(data):
    # Assume your data has 14 columns: 'fighter_height', 'fighter_weight', 'fighter_age', 'fighter_reach', 'fighter_leg_reach', 'fighter_striking_accuracy', 'fighter_takedown_accuracy', 'opponent_height', 'opponent_weight', 'opponent_age', 'opponent_reach', 'opponent_leg_reach', 'opponent_striking_accuracy', 'opponent_takedown_accuracy', 'victory'
    X = data[:, :14]
    y = data[:, 14]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create a random forest classifier
    model = RandomForestClassifier()

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Measure the model's performance
    from sklearn.metrics import accuracy_score, precision_score, recall_score
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    return y_pred