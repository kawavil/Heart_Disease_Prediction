import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class Preprocess:

    def __init__(self):
        pass

    def convert_to_num(self, df):
        self.df = df
        try:
            for col in self.df.columns:
                if self.df[col].dtype == 'O':
                    self.df[col] = pd.to_numeric(self.df[col])
            return self.df
        except Exception as e:
            print("Error occurred while converting object to number")
            raise Exception()

    def scale(self, df):
        self.df = df

        try:
            scalar = StandardScaler()
            X = df.iloc[:, :-1]
            y = df.iloc[:, -1]
            X = scalar.fit_transform(X)
            X = pd.DataFrame(X, columns=self.df.columns[:-1])
            df = pd.concat([X, y], axis=1)
            return df
        except Exception as e:
            print("Error while  scaling the data")
            raise Exception()


#if __name__ == 'main':
df = pd.read_csv("C:/Users/Vilas/Documents/Projects/Heart Disease Prediction/Data/heart.csv")
preprocess = Preprocess()
df = preprocess.convert_to_num(df)
print(df.head())
print(df.dtypes)
#df = preprocess.scale(df)
##print(df.head())

