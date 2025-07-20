import pandas as pd

def create_dataframe():
   
    data = {'Marks': [45, 67, 88, 32, 76]}
    return pd.DataFrame(data)

def apply_condition(df, column_name):
    
    
    df[column_name] = df[column_name].where(df[column_name] >= 50, 'Fail')
    return df

def main():
   
    df = create_dataframe()
    print("Original DataFrame:\n", df)

    
    df_updated = apply_condition(df, 'Marks')

   
    print("\nUpdated DataFrame:\n", df_updated)

if __name__=="__main__":

    main()