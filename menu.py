import PublisherSalesPerRegion as PubSales
import GenreCriticScores as GenreScores


import GenreSalesNA as PieData
import SalesbyRegion as RegSales
import dataCallum as dc

def main_menu():
    print("--MENU--")
    print("1. Display Critic Score Data for Genres")
    print("2. Display 10 highest critically scored games")
    print("3. Display top 5 selling publishers per region")
    print("4. Display regions with most games sold")
    print("5. Display sales by genre")
    print("6. Exit")

loop=True

while loop:
    main_menu()
    choice = int(input("Enter your choice [1-6]: "))
    if choice==1:
        #Dom's Code
        criticScoreLoop = True
        loop=False
        criticScoreOption = 0
        while criticScoreLoop:
            print("Select the option to display.")
            print("1. Mean Critic Scores")
            print("2. Top 3 Genres with Highest Total Critic Score")
            print("3. Bottom 3 Genres with Lowest Total Critic Score")
            print("4. Quit")
            criticScoreOption = int(input())
            if criticScoreOption==1:
                GenreScores.genreCriticScores("Mean_Scores")
                publisherSalesLoop = False
                loop=False
            elif criticScoreOption==2:
                GenreScores.genreCriticScores("Top_3")
                publisherSalesLoop = False
                loop=False
            elif criticScoreOption==3:
                GenreScores.genreCriticScores("Bottom_3")
                publisherSalesLoop = False
                loop=False
            elif criticScoreOption==4:
                print("Exiting...")
                quit()
            else:
                print("Error: Invalid Option")
                quit()
        
    elif choice==2:
        #Callum's code
        dc.dataCallum()
        loop=False
    elif choice==3:
        #Louis' code
        publisherSalesLoop = True
        loop=False
        publisherRegionChoice = 0
        while publisherSalesLoop:
            print("Select the region to display.")
            print("1. North America")
            print("2. Europe")
            publisherSalesChoice = int(input())
            if publisherSalesChoice==1:
                PubSales.top5PublisherSales("NA_Sales")
                publisherSalesLoop = False
                loop=False
            elif publisherSalesChoice==2:
                PubSales.top5PublisherSales("EU_Sales")
                publisherSalesLoop = False
                loop=False
            else:
                print("Error: Invalid Option")
                quit()
    #Charlie's Code
    elif choice==4:
        print ("Sales by Region")
        loop=False
        RegSales.SalesbyRegion()
    elif choice==5:
        PieData.genreToSales()
        loop=False
    elif choice==6:
        print ("Exiting...")
        loop=False
    else:
        print("Invalid selection!")

print ("Exiting...")
	