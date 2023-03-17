import pandas as pd
import matplotlib as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")


def developerSales(global):
    #Group the data based on the developer column and sum that data up. Specifying the data found in the NA_Sales column.
    developerSales = DATA.groupby("Developer").sum(numeric_only=True)[global].reset_index()
    #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
    developerSales = developerSales.sort_values(global, ascending=False).head(5)
    #print(publisherSales)
    return developerSales


def graphSales(global):
    salesData = developerSales(global)
    print(salesData)


graphSales("EU_Sales")



# test = developerSales("global")
# print(test)
