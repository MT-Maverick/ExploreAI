import numpy as np 
import pandas as pd

def print_summary(data):
      print('Data Summary:')
      print(data.describe())

def get_highest_precipitation_month(data):
    """
    Get the month with the highest precipitation.
    """
    if "Precipitation" not in data.columns or "Category" not in data.columns:
        raise ValueError("The required columns 'Precipitation' and 'Category' are missing.")

    max_precip_row = data.loc[data["Precipitation"].idxmax()]
    return max_precip_row["Month"]

def column_stats(data, column):
	"""Calculate mean, median, and standard deviation for a specified column."""
	values = data[column].to_numpy()
	mean = np.mean(values)
	median = np.median(values)
	std_dev = np.std(values)
	return {"mean": mean, "median": median,  "std_dev": std_dev}
