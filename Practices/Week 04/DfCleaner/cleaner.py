import pandas as pd

class Cleaner:
    def __init__(self, df):
        self.df = df

    def drop_empty(self):
        self.df = self.df.dropna()
    
    def fill_empty(self, column_name):
        self.df[column_name] = self.df[column_name].fillna(self.df[column_name].mean())
    
    def drop_column(self, column_name):
        self.df = self.df.drop(columns=column_name)
    
    def fix_index(self):
        self.df = self.df.reset_index(drop=True)
    
    def fix_dates(self, column_name):
        self.df[column_name] = pd.to_datetime(self.df[column_name])