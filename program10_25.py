import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataframe():
    
    data = {
        'Age': [25, 30, 45, 35, 22],
        'Salary': [50000, 60000, 80000, 65000, 45000],
        'Purchased': [1, 0, 1, 0, 1]
    }
    return pd.DataFrame(data)

def split_data(df):
    
    X = df[['Age', 'Salary']]    
    y = df['Purchased']             
    return train_test_split(X, y, test_size=0.3, random_state=1)

def display_result(X_train, X_test, y_train, y_test):
    
    print("X_train:\n", X_train)
    print("\nX_test:\n", X_test)
    print("\ny_train:\n", y_train)
    print("\ny_test:\n", y_test)

def main():
   
    df = create_dataframe()
    print("Original DataFrame:\n", df)

   
    X_train, X_test, y_train, y_test = split_data(df)

    
    display_result(X_train, X_test, y_train, y_test)

if __name__=="__main__":

    main()