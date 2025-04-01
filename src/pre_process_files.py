import pandas as pd
from src.llm_functions import table_cleaner

def clean_empty_rows(df):
  rows_to_drop = []
  for i in range(len(df)):
    non_nan_count = 0
    for j in range(len(df.columns)):

      if pd.isna(df.iloc[i,j]) == False:
        non_nan_count+=1

    if non_nan_count == 0:
      rows_to_drop.append(i)
  df = df.drop(rows_to_drop)

  return df

def clean_empty_columns(df):
  columns_to_drop = []
  for j in (df.columns):
    non_nan_count = 0
    for i in range(len(df)):
      if pd.isna(df.loc[i,j]) == False:
        non_nan_count+=1

    if non_nan_count == 0:
      columns_to_drop.append(j)
  df = df.drop(columns=columns_to_drop)

  return df

def pre_process_file(file):

  if ".xls" in file.name:
    data = pd.read_excel(file)
  elif ".csv" in file.name:
    data = pd.read_csv(file)

  data = clean_empty_columns(data)
  data = clean_empty_rows(data)
  data_markdown = data.to_markdown(index=False)
  clean_table = table_cleaner(data_markdown)

  return clean_table

    
