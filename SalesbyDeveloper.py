import pandas as pd
import matplotlib.pyplot as matplot

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")
def main_menu():
    print("--MENU--")
    print("1. Global")
    print("2. Europe")
    print("3. North America")
    print("4. Japan")
    print("5. Other")
    print("6. Exit")

loop=True

while loop:
    main_menu()
    choice = int(input("Enter your choice [1-6]: "))

    if choice==1:
        print ("Global Selected")
        loop=False
    elif choice==2:
        print ("Europe Selected")
        loop=False
    elif choice==3:
        print ("North America Selected")
        loop=False
    elif choice==4:
        print ("Japan Selected")
        loop=False
    elif choice==5:
        print("Other Selected")
        loop=False
    elif choice==6:
        print ("Exiting...")
        loop=False
    else:
        print("Invalid selection!")

def top_5_developer_sales(globals):


    #Check to see what region has been selected
    if choice==1:
        print ("Global Selected")
        loop=False

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
    
    elif choice==2:
        print ("Global Selected")
        loop=False

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

top_5_developer_sales("Global_Sales")

elif choice==3:
print ("North America Selected")
loop=False
        
developer_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
developer_data = developer_data.sort_values(globals, ascending=False).head(5)
developer_names = developer_data.Developer
game_sales = developer_data.NA_Sales
        
        #Set up the bar chart
matplot.bar(developer_names, game_sales)

        #Set graph labels and title.
matplot.title("Best Selling Developer in North America")
matplot.xlabel("Developer")
matplot.ylabel("Sales")
        
        #Show the bar chart
matplot.show()

top_5_developer_sales("NA_Sales")

 elif choice==4:
print("Japan Selected")
loop=False

developer_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
developer_data = developer_data.sort_values(globals, ascending=False).head(5)
developer_names = developer_data.Developer
game_sales = developer_data.JP_Sales
        
        #Set up the bar chart
matplot.bar(developer_names, game_sales)

        #Set graph labels and title.
matplot.title("Best Selling Developer in Japan")
matplot.xlabel("Developer")
matplot.ylabel("Sales")
        
        #Show the bar chart
matplot.show()

top_5_developer_sales("Japan_Sales")

elif choice==5:
print ("Other Selected")
loop=False

developer_data = DATA.groupby("Developer").sum(numeric_only=True)[globals].reset_index()

        #Sort the data into descending order. Starting from the the best selling publishers. Limit the data to the top 5 publishers.
developer_data = developer_data.sort_values(globals, ascending=False).head(5)
developer_names = developer_data.Developer
game_sales = developer_data.Other_Sales
        
        #Set up the bar chart
matplot.bar(developer_names, game_sales)

        #Set graph labels and title.
matplot.title("Best Selling Developer in Other Reigon")
matplot.xlabel("Developer")
matplot.ylabel("Sales")
        
        #Show the bar chart
matplot.show()

top_5_developer_sales("Other_Sales")
