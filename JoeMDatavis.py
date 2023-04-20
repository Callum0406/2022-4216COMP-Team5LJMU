import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
import numpy as np
##Using jupyter to run piechart on the fly.
import jupyter as jup

## Sales by Genre Pie Chart


def genreToSales(userRegion):

    data = pd.read_csv("Tagged-Data-Final.csv")
    #Creating a data variable to store the read data.


    #Creating an if/elif to choose between regions to display.
    if userRegion == "NA_Sales":

        #Data grouped up by genre, sorted and limited to 5.
        salesRegion = "NA_Sales"
        compiled_data = data.groupby("Genre").sum(numeric_only=True)[salesRegion].reset_index()
        compiled_data = compiled_data.sort_values(salesRegion, ascending=False).head(5)

        genre_label = compiled_data.Genre
        region_name = compiled_data.NA_Sales

        #Segment to design how the pie chart looks.
        #Explode will space out each segment, plt.show() displays the chart to user.
        plt.pie(region_name, labels=genre_label, autopct='%1.1f%%', 
                explode=(0.1,0.05,0.05,0.1,0.07), shadow=True, 
                colors=['#485696','#e34a6f','#f7934c','#80ded9','#a682ff'])             
        plt.title('Top 5 NA Sales by Genre')        
        plt.axis('equal')
        plt.show()

        #This segment is identical to NA sales, so all comments above apply.
    elif userRegion == "EU_Sales":

        salesRegion = "EU_Sales"
        compiled_data = data.groupby("Genre").sum(numeric_only=True)[salesRegion].reset_index()
        compiled_data = compiled_data.sort_values(salesRegion, ascending=False).head(5)

        genre_label = compiled_data.Genre
        region_name = compiled_data.EU_Sales

        plt.pie(region_name, labels=genre_label, autopct='%1.1f%%', 
                explode=(0.1,0.05,0.05,0.1,0.07), shadow=True, 
                colors=['#d4afb9','#3777ff','#af3e4d','#52ffb8','#f9df74'])
        plt.title('Top 5 EU Sales by Genre')
        
        plt.axis('equal')
        plt.show()