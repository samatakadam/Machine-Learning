import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def display_student_info(data):
    #1
    df = pd.DataFrame(data)
    print("Shape of DataFrame:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data types:\n", df.dtypes)
    #2
    print("Discribed data is :\n",df.describe())
    #3
    df['Total']=df['Math']+df['Science']+df['English']
    print("updated dataframe is :")
    print(df)
    #4
    Highest_Scorer=df[df['Science']>85]
    print(Highest_Scorer)
    #5
    df['Name']=df['Name'].replace('Pooja','Puja')
    print(df)
    #6
    sorted_df=df.sort_values(by='Total',ascending=False)
    print(sorted_df)
    #7
    plt.figure(figsize=(8,5))
    plt.bar(df['Name'],df['Total'],color='Violet')
    plt.xlabel('Student Name ')
    plt.ylabel('Total Marks')
    plt.title('Total Marks of Student')
    plt.tight_layout()
    plt.show()
    #8

    Amit_Marks=df[df['Name']=='Amit']
    print(df)


    plt.figure(figsize=(8,5))
    plt.plot(['Math', 'Science', 'English'], Amit_Marks[['Math', 'Science', 'English']].values[0])
    plt.title("Amit's Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()
    #9
    # missing values
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
            }


    df2 = pd.DataFrame(data2)


    df2[['Math', 'Science']] = df2[['Math', 'Science']].fillna(df2[['Math', 'Science']].mean())


    print(df2)

student_data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],      
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}


display_student_info(student_data)

