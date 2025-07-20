import pandas as pd
import numpy as np

def create_dataframe():
    
    data = {'Marks': [85, np.nan, 90, np.nan, 95]}
    return pd.DataFrame(data)

def interpolate_missing_values(df, column_name):
   
    df[column_name] = df[column_name].interpolate(method='linear')
    return df

def main():
   
    df = create_dataframe()
    print("Original DataFrame:\n", df)

   
    df_filled = interpolate_missing_values(df, 'Marks')

  
    print("\nInterpolated DataFrame:\n", df_filled)


if __name__=="__main__":

    main()