import pandas as pd

def load_data():
    df1 = pd.read_csv("data/file1.csv")
    df2 = pd.read_csv("data/file2.csv")
    return df1, df2

def get_numeric_columns(df):
    return df.select_dtypes(include=["int64", "float64"]).columns.tolist()

def merge_data(df1, df2, column):
    return pd.merge(df1, df2, on=column, suffixes=("_File1", "_File2"))