import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    fig ,ax = plt.subplots()
    plt.scatter(x = df['Year'],y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(x = df['Year'],y = df['CSIRO Adjusted Sea Level'])
    x_prediction = pd.Series([i for i in range (1880,2050)])
    y_prediction = res.slope * x_prediction + res.intercept
    plt.plot(x_prediction, y_prediction ,'r')
    # Create second line of best fit
    bestFit = df.loc(df['Year'] >= 2000)
    newx = bestFit.Series([i for i in range (2000,2050)])
    newy = res.slope * newx + res.intercept
    plt.plot(newx , newy , 'green')

    # Add labels and title
    ax.set_xlable('Year')
    ax.set_ylable('CSIRO Adjusted Sea Level')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()