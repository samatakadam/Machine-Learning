import pandas as pd

def create_dataframe():
    
    data = {'Age': [18, 22, 25, 30, 35]}
    return pd.DataFrame(data)

def min_max_scale(df, column_name):

    min_val = df[column_name].min()
    max_val = df[column_name].max()
    df[column_name + '_Scaled'] = (df[column_name] - min_val) / (max_val - min_val)
    return df

def main():
    
    df = create_dataframe()
    print("Original DataFrame:\n", df)

    df_scaled = min_max_scale(df, 'Age')

   
    print("\nScaled DataFrame:\n", df_scaled)

if __name__=="__main__":

    main()