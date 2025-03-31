import pandas as pd
from pre_processing import *
from ll_functions import table_cleaner

def pre_process_file(file_path):

  if ".xls" in file_path:
    data = pd.read_excel(file_path)
  elif ".csv" in file_path:
    data = pd.read_csv(file_path)

  
    
