import pandas as pd
import matplotlib.pyplot as plt
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
    #4
    sagar_marks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].values[0]

    plt.figure(figsize=(8,5))
    plt.pie(sagar_marks, labels=['Math', 'Science', 'English'], autopct='%1.1f%%', startangle=90)#startangle =clockwise #%-for decimaland whole number.
    plt.title("Sagar's Subject-wise Marks")
    plt.tight_layout()
    plt.show()

    #5
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

    print(df)
    #6
    pass_count = (df['Status'] == 'Pass').sum()
    print("Number of students who passed:", pass_count)

    #7
    df.to_csv('student_results.csv', index=False)
    #8
    plt.hist(df['Math'], bins=5, color='Violet', edgecolor='black')
    plt.title('Distribution of Math Marks')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.show()
    #9
    df.rename(columns={'Math': 'Mathematics'}, inplace=True)
    print(df)
    #10
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))# patch_artist-color,#boxprops=dict-style 
    
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()


    







if __name__=="__main__":
    main()