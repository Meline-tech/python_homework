import numpy as np
def array_mean(arr):
    return  np.mean(arr)
import pandas as pd

def read_file_with_pandas(filename):
  df=pd.read_csv(filename)
  return df

   while True:
    input_data= input("Innput any data")
    if input_data == "break"
        print("The programm is finished ")
        break