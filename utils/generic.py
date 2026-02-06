def min_max(arr)    :
    return np.min(arr), np.max(arr)
import numpy as np
def array_mean(arr):
    return  np.mean(arr)
import pandas as pd

def read_file_with_pandas(filename):
  df=pd.read_csv(filename)
  return df
import pandas as pd
def column_value(df, column_name):
    return df[column_name].values

