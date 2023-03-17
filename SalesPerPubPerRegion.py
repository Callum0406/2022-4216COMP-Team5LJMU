import pandas as pd

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")


def publisherSales(region):
    #Group the data based on the publisher column and sum that data up. Specifying the data found in the NA_Sales column.
    publisherSales = DATA.groupby("Publisher").sum(numeric_only=True)[region].reset_index()
    #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
    publisherSales = publisherSales.sort_values(region, ascending=False).head(5)
    print(publisherSales)



publisherSales("NA_Sales")
print("----")
publisherSales("EU_Sales")