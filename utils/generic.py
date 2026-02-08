def min_max(arr)    :
    return np.min(arr), np.max(arr)
import numpy as np
def array_mean(arr):
    return  np.mean(arr)
import pandas as pd

def read_file_with_pandas(filename):
  df=pd.read_csv(filename)
  return df
def column_values(df, column_name):
    return df[column_name]
file_name="/content/sample_data/mnist_train_small.csv"
col_name="6"
df=read_file_with_pandas(file_name)
col_data=column_values(df, col_name)
maximum=min_max(col_data)
minimum=min_max(col_data)
average=array_mean(col_data)
print (f"max={maximum} , min={minimum}, mean={average}" )

