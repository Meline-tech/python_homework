import numpy as np
def array_mean(arr):
    return  np.mean(arr)
import pandas as pd

def read_file_with_pandas(filename):
  df=pd.read_csv(filename)
  return df
