###############################################
#
# Required Python Packages
#
###############################################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#####################################################
# FilePaths
#####################################################

INPUT_PATH = "Diabities.data"
OUTPUT_PATH = "Diabities.csv"

#############################################
# Function Name:       read_data
# Description:         Read the data into pandas dataframe
# Input:               path of CSV file
# Output:              gives the data
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
###########################################

def read_data(path):
    """Read the data into pandas dataframe"""
    data = pd.read_csv(path, header=None)
    return data

##################################################
# Function Name:       Data Exploration
# Description:         Doing Basic Operations on data
# Input:               Dataset 
# Output:              shape, columns, head of dataset
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def explore_data(data):
    """Print basic information about the dataset."""
    print("Columns:")
    print(data.columns)
    print("\nHead:")
    print(data.head())
    print("\nShape:")
    print(data.shape)

##################################################
# Function Name:       Droping Column
# Description:         Dropping a column 'Outcome'
# Input:               Dataset with outcome column
# Output:              Dataset without that column
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def drop_column(data):
    """Drop the Outcome column and return features and target"""
    X = data.drop(columns=['Outcome'])
    Y = data['Outcome']
    print("\nFeature Shape:", X.shape)
    print("Target Shape:", Y.shape)
    return X, Y

##################################################
# Function Name:       split_dataset
# Description:         Split the dataset with train_percentage
# Input:               Dataset with related information
# Output:              Dataset after splitting
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def split_dataset(dataset, train_percentage, feature_header, target_header, random_state=42):
    """Split dataset into train/test"""
    X_train, X_test, Y_train, Y_test = train_test_split(
        dataset[feature_header], dataset[target_header],
        train_size=train_percentage, random_state=random_state,
        stratify=dataset[target_header]
    )
    return X_train, X_test, Y_train, Y_test

##################################################
# Function Name:       Model Training
# Description:         Model training of given dataset
# Input:               Splitted dataset
# Output:              Trained model
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def train_model(X_train, Y_train):
    """Train a logistic regression model."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    return model

##################################################
# Function Name:       Model Evaluation
# Description:         Testing of dataset and accuracy
# Input:               Trained model and datasets
# Output:              Accuracy scores
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def evaluate_model(model, X_train, Y_train, X_test, Y_test):
    """Print training and testing accuracy."""
    print("\nModel Performance:")
    print(f"Training Accuracy: {model.score(X_train, Y_train)}")
    print(f"Testing Accuracy: {model.score(X_test, Y_test)}")

##################################################
# Function Name:       Main 
# Description:         Main function where execution starts 
# Author:              Samata Kalyan Kadam
# Date:                10/8/2025
#################################################

def main():
    filepath = "diabetes.csv"  
    data = pd.read_csv(filepath)  
    explore_data(data)
    X, Y = drop_column(data)
    data['Outcome'] = Y  
    feature_header = X.columns.tolist()
    target_header = 'Outcome'
    X_train, X_test, Y_train, Y_test = split_dataset(data, 0.8, feature_header, target_header)
    model = train_model(X_train, Y_train)
    evaluate_model(model, X_train, Y_train, X_test, Y_test)

#################################################
# Starter function
#################################################
if __name__ == "__main__":
    main()