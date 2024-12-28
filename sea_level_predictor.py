import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
     # Read data from file
    df = pd.read_csv('Data Science Certification Projects/Sea Level Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    Xi = np.arange(df['Year'].min(),2050,1)
    Yi = Xi*fit1.slope + fit1.intercept

    plt.plot(Xi,Yi)

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    fit2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    Xj = np.arange(2000,2050,1)
    Yj = Xj*fit2.slope + fit2.intercept

    plt.plot(Xj,Yj)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
