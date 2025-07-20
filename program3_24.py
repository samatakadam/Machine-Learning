import pandas as pd

def normalize_math(df):
    min_val=df['Math'].min()
    max_val=df['Math'].max()
    df['Math_Normalized']=(df['Math']-min_val/(max_val-min_val))
    return df

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Puja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender': ['Male', 'Male', 'Female']

    }
    df=pd.DataFrame(data)
    df=normalize_math(df)

    print(df[['Name', 'Math', 'Math_Normalized']])

    #2
    df_encoded = pd.get_dummies(df, columns=['Gender'],dtype=int)

    print(df_encoded)
    #3
    
    Avg_marks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print(Avg_marks)




if __name__=="__main__":
    main()