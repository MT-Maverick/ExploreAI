import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def rename_cols(data):
    print("Current columns:")
    print(data.head(5))
    data = data.rename(columns={'Category': 'Month', 
                        'Average Minimum Surface Air Temperature': 'min_temp',
                        'Average Mean Surface Air Temperature': 'mean_temp',
                        'Average Maximum Surface Air Temperature': 'max_temp'})
    print("Updated column names: ")
    print(data.columns)
    return data
