import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def MarvellousAdvertise(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset sample is : ")
    print(df.head())

    print("Clean the dataset")
    df.drop(columns = ['Unnamed: 0'] , inplace = True) 

    print("Updated dataset is : ")
    print(df.head())

    

    

    
    

    x = df[['TV', 'radio', 'newspaper']]
    y = df['sales']
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.2, random_state = 42)

    model = LinearRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    results = pd.DataFrame({
        'Predicted Sales': y_pred,
        'Expected Sales': y_test.values
    })

    print("\nTop 10 Predicted vs Expected Sales Values:\n")
    print(results.head(10))


   

  

   
    
def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()