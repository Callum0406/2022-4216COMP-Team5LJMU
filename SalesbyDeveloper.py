import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")


def top_5_developer_sales(globals):


    #Check to see what region has been selected
    if globals == "Global":

        #Group the data based on the publisher column and sum that data up. Specifying the data found in the NA_Sales column.
        developer_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        developer_data = developer_data.sort_values(globals, ascending=False).head(5)

        #Get the values for the chart
        developer_names = developer_data.Developer
        game_sales = developer_data.globals

        #Set up the bar chart
        matplot.bar(developer_names, game_sales)


        #Set graph labels and title.
        matplot.title("Best Selling Developers in North America")
        matplot.xlabel("Developers")
        matplot.ylabel("Sales")

        #Show the bar chart
        matplot.show()
    
    elif globals == "EU_Sales":

        developer_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
        developer_data = developer_data.sort_values(globals, ascending=False).head(5)
        developer_names = developer_data.Developer
        game_sales = developer_data.EU_Sales
        
        #Set up the bar chart
        matplot.bar(developer_names, game_sales)

        #Set graph labels and title.
        matplot.title("Best Selling Developer in Europe")
        matplot.xlabel("Developer")
        matplot.ylabel("Sales")
        
        #Show the bar chart
        matplot.show()

top_5_developer_sales("EU_Sales")

if globals == "NA_Sales":

    dev_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
dev_data = dev_data.sort_values(globals, ascending=False).head(5)
dev_names = dev_data.Developer
game_sales = dev_data.NA_Sales
        
        #Set up the bar chart
matplot.bar(dev_names, game_sales)

        #Set graph labels and title.
matplot.title("Best Selling Developer in North America")
matplot.xlabel("Developer")
matplot.ylabel("Sales")
        
        #Show the bar chart
matplot.show()

top_5_developer_sales("NA_Sales")
