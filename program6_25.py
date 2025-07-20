import pandas as pd

def create_dataframe():
    
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    return pd.DataFrame(data)

def replace_grades(df):

    replacement_dict = {
        'A+': 'Excellent',
        'A': 'Very Good',
        'B+': 'Good',
        'B': 'Average',
        'C': 'Poor'
    }
    df['Grade'] = df['Grade'].replace(replacement_dict)
    return df

def main():
   
    df = create_dataframe()
    print("Original DataFrame:\n", df)

 
    df_updated = replace_grades(df)
    
    
    print("\nUpdated DataFrame:\n", df_updated)

if __name__=="__main__":

    main()