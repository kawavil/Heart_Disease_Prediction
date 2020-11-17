import pandas as pd
import numpy as np


class Preprocess:

    def __init__(self):
        pass

    def convert_to_num(self, df):
        self.df = df
        try:
            for col in self.df.columns:
                if self.df[col].dtype == 'Object':
                    self.df[col] = pd.to_numeric(self.df[col])
            return self.df
        except Exception as e:
            print("Error occurred while converting object to number")
            raise Exception()


if __name__ == 'main':
    df = pd.read_csv("../Data/heart.csv")
    preprocess = Preprocess()
    df = preprocess.convert_to_num(df)
