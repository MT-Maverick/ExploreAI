import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_precipitation(data):
    plt.bar(data['Month'], data['Precipitation'], color='skyblue')
    plt.title('Monthly Precipitation')
    plt.xlabel('Month')
    plt.ylabel('Precipitation (mm)')
    plt.show()

def visualize_temps(data):
    fig, ax = plt.subplots(figsize = (8,8))
    annual_avg = np.mean(data['mean_temp'].to_numpy())
    # Plot temperatures
    ax.plot(data['Month'], data['min_temp'], color="green", label="Min Temperature")
    ax.plot(data['Month'], data['mean_temp'], color="blue", label="Mean Temperature")
    ax.plot(data['Month'], data['max_temp'], color="red", label="Max Temperature")
    
    # Add a horizontal line for annual average temperature
    ax.axhline(y=annual_avg, color="purple", linestyle="--", label="Annual Average")
    ax.fill_between(
        data['Month'], 
        data['mean_temp'], 
        annual_avg, 
        where=(data['mean_temp'] > annual_avg), 
        interpolate=True, 
        color="red", 
        alpha=0.25, 
        label="Hot (Above Avg)"
    )
    ax.fill_between(
        data['Month'], 
        data['mean_temp'], 
        annual_avg, 
        where=(data['mean_temp'] < annual_avg), 
        interpolate=True, 
        color="green", 
        alpha=0.25, 
        label="Cool"
    )
    plt.title('Temperature Trends')
    plt.xlabel('Month')
    plt.ylabel('Temperature (C)')
    ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
    plt.tight_layout()
    plt.show()