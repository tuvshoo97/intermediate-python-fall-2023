# import pandas as pd

# def drop_empty(df):
#     return df.dropna()

# def fill_empty(df, column_name):
#     return df[column_name].fillna(df[column_name].mean())

# def drop_column(df, column_name):
#     return df.drop(columns=column_name)

# def fix_index(df):
#     return df.reset_index(drop=True)

# def fix_dates(df, column_name):
#     return pd.to_datetime(df[column_name])