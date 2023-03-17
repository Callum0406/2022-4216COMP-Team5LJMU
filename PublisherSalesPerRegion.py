import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")


def top_5_publisher_sales_NA(region):


    #Check to see what region has been selected
    if region == "NA_Sales":
        #Group the data based on the publisher column and sum that data up. Specifying the data found in the NA_Sales column.
        publisher_data = DATA.groupby("Publisher").sum(numeric_only=True)[region].reset_index()
        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        publisher_data = publisher_data.sort_values(region, ascending=False).head(5)

        #Get the values for the chart
        publisher_names = publisher_data.Publisher
        game_sales = publisher_data.NA_Sales

        #Set up the bar chart
        matplot.bar(publisher_names, game_sales)


        #Set graph labels and title.
        matplot.title("Best Selling Publishers in North America")
        matplot.xlabel("Publishers")
        matplot.ylabel("Sales")

        #Show the bar chart
        matplot.show()
    
    elif region == "EU_Sales":

        publisher_data = DATA.groupby("Publisher").sum(numeric_only=True)[region].reset_index()
        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        publisher_data = publisher_data.sort_values(region, ascending=False).head(5)

        publisher_names = publisher_data.Publisher
        game_sales = publisher_data.EU_Sales
        
        #Set up the bar chart
        matplot.bar(publisher_names, game_sales)

        #Set graph labels and title.
        matplot.title("Best Selling Publishers in North America")
        matplot.xlabel("Publishers")
        matplot.ylabel("Sales")
        
        #Show the bar chart
        matplot.show()

top_5_publisher_sales_NA("EU_Sales")
