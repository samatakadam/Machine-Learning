import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def PlayPredictor(Datapath):
    # Load and encode data
    df = pd.read_csv(Datapath)
    print("Data Loaded Successfully")
    print(df.head())

    le_whether = LabelEncoder()
    le_temperature = LabelEncoder()
    le_play = LabelEncoder()

    df['Whether'] = le_whether.fit_transform(df['Whether'])
    df['Temperature'] = le_temperature.fit_transform(df['Temperature'])
    df['Play'] = le_play.fit_transform(df['Play'])

    print("Encoded Data is :")
    print(df.head())

    features = df[['Whether', 'Temperature']]
    labels = df['Play']

    # Scale features
    scaler = StandardScaler()
    x_scale = scaler.fit_transform(features)

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(x_scale, labels, test_size=0.2, random_state=42)

    # Find best k
    accuracy_scores = []
    k_range = range(1, 21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)

    best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is :", best_k)

    # Final model
    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Final best accuracy is :", accuracy * 100)
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

def main():
    PlayPredictor("PlayPredictor.csv")

if __name__=="__main__":
    main()