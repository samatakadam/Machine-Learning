import pandas as pd
import matplotlib.pyplot as plt

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
    


student_data = {
    'Name': ['Arnit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],      
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}


display_student_info(student_data)