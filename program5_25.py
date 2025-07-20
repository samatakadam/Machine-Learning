import pandas as pd
from sklearn.model_selection import train_test_split

def create_dataframe():
   
    data = {
        'Age': [22, 25, 47, 52, 46, 56],
        'Purchased': [0, 1, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def split_dataframe(df, test_size=0.3, random_state=1):
    
    X = df[['Age']]          
    y = df['Purchased']      
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def display_split(X_train, X_test, y_train, y_test):
    
    print("X_train:\n", X_train)
    print("\nX_test:\n", X_test)
    print("\ny_train:\n", y_train)
    print("\ny_test:\n", y_test)

def main():
    
    df = create_dataframe()
    print("Original DataFrame:\n", df)

   
    X_train, X_test, y_train, y_test = split_dataframe(df)

   
    display_split(X_train, X_test, y_train, y_test)

if __name__=="__main__":

    main()