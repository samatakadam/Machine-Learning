import pandas as pd
import numpy as np
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import precision_score,recall_score,precision_recall_fscore_support,f1_score,confusion_matrix
def main():
    diabetes = pd.read_csv("diabetes.csv")

    print(diabetes.columns)

    print(diabetes.head())

    print(diabetes.shape)

    print(diabetes.describe())

    X = diabetes.drop(columns = ['Outcome'])
    Y = diabetes['Outcome']

    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

    print(X.shape)
    print(Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    logreg = LogisticRegression().fit(X_train,Y_train)

    print("Training Accuracy : ")
    print(logreg.score(X_train,Y_train))

    print("Testing Accuracy : ")
    print(logreg.score(X_test,Y_test))

    plt.hist(diabetes['Age'],bins=10,color="skyblue",edgecolor='black')
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.title("Distribution of Age")
    plt.grid(True)
    plt.show()

    selected_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Age']
    plt.figure(figsize=(12, 6))
    diabetes[selected_columns].boxplot()
    plt.title('Boxplot of Selected Features')
    plt.ylabel('Value Range')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

   
   
    sns.pairplot(diabetes, vars=selected_columns, hue='Outcome', palette='coolwarm')
    plt.suptitle('Pairplot of Features Colored by Outcome', y=1.02)
    plt.show()

    model = LogisticRegression()
    model.fit(X_train, Y_train)
    preds = model.predict(X_test)
    print("Logistic Regression")
    print("Accuracy:", accuracy_score(Y_test, preds))
    print(classification_report(Y_test, preds))

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, Y_train)
    preds = model.predict(X_test)
    print("\n Decision Tree Classifier")
    print("Accuracy:", accuracy_score(Y_test, preds))
    print(classification_report(Y_test, preds))

    predictions=model.predict(X_test)
    print(" Accuracy:", accuracy_score(Y_test, predictions))
    print(" Precision:", precision_score(Y_test, predictions))
    print(" F1 Score:", f1_score(Y_test, predictions))
    print(" Recall:", recall_score(Y_test, predictions))
    
    cm = confusion_matrix(Y_test, predictions)

    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["No Diabetes", "Diabetes"], yticklabels=["No Diabetes", "Diabetes"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("📊 Confusion Matrix - Logistic Regression")
    plt.tight_layout()
    plt.show()

    result = pd.DataFrame(X_test, columns=X.columns)
    result['Predicted_Outcome'] = predictions

    print(result.head())


    result.to_csv("diabetes_predictions.csv", index=False)






if __name__ == "__main__":
    main()