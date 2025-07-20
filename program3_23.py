import pandas as pd


def display_student_info(data):
    df = pd.DataFrame(data)
    print("Shape of DataFrame:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data types:\n", df.dtypes)
    print("Discribed data is :\n",df.describe())
    df['Total']=df['Math']+df['Science']+df['English']
    print("updated dataframe is :")
    print(df)
    


student_data = {
    'Name': ['Arnit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],      
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}


display_student_info(student_data)