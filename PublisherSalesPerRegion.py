import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")


def top5publisherSalesNA(region):


    #Check to see what region has been selected
    if region == "NA_Sales":
        #Group the data based on the publisher column and sum that data up. Specifying the data found in the NA_Sales column.
        publisherData = DATA.groupby("Publisher").sum(numeric_only=True)[region].reset_index()
        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        publisherData = publisherData.sort_values(region, ascending=False).head(5)

        #Get the values for the chart
        publisherNames = publisherData.Publisher
        gameSales = publisherData.NA_Sales
    
        
        #Set up the bar chart
        matplot.bar(publisherNames, gameSales)

        #Set graph labels and title.
        matplot.xlabel("Publishers")
        matplot.ylabel("Sales")
        #matplot.title("Total Sales in North America")

        #Show the bar chart
        matplot.show()
    
    elif region == "EU_Sales":

        publisherData = DATA.groupby("Publisher").sum(numeric_only=True)[region].reset_index()
        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        publisherData = publisherData.sort_values(region, ascending=False).head(5)

        publisherNames = publisherData.Publisher
        gameSales = publisherData.EU_Sales
        
        #Set up the bar chart
        matplot.bar(publisherNames, gameSales)

        #Set graph labels and title.
        matplot.xlabel("Publishers")
        matplot.ylabel("Sales")
        #matplot.title("Total Sales in North America")

        #Show the bar chart
        matplot.show()

top5publisherSalesNA("EU_Sales")