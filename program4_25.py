import pandas as pd

def create_dataframe():
    
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    return pd.DataFrame(data)

def one_hot_encode(df, column_name):
   
    return pd.get_dummies(df, columns=[column_name])

def main():
    
    df = create_dataframe()
    print("Original DataFrame:\n", df)

    
    df_encoded = one_hot_encode(df, 'Department')

    
    print("\nOne-Hot Encoded DataFrame:\n", df_encoded)


if __name__=="__main__":

    main()