import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Sales by Genre Pie Chart

def genreToSales():
    #Creating a data variable to store the read data.
    data = pd.read_csv("Tagged-Data-Final.csv")

    salesRegion = "NA_Sales"
    #Data grouped up by genre, sorted and limited to 5.
    compiled_data = data.groupby("Genre").sum(numeric_only=True)[salesRegion].reset_index()
    compiled_data = compiled_data.sort_values(salesRegion, ascending=False).head(5)

    genre_label = compiled_data.Genre
    region_name = compiled_data.NA_Sales
    #Creating a pie chart.
    plt.pie(region_name, labels=genre_label, autopct='%1.1f%%')
    plt.title('Top 5 NA Sales by Genre')
    plt.axis('equal')
    plt.show()
