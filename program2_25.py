import pandas as pd

def detect_column_types(df):
    
    return df.dtypes

def convert_age_to_int(df):
    
    if df['Age'].dtype == float:
        df['Age'] = df['Age'].astype(int)
    return df

def main():
    
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
    df = pd.DataFrame(data)
    
    
    print("Before conversion:\n", detect_column_types(df))
    
    
    df = convert_age_to_int(df)

   
    print("\nAfter conversion:\n", detect_column_types(df))

    
    print("\nFinal DataFrame:\n", df)

if __name__=="__main__":
    main()