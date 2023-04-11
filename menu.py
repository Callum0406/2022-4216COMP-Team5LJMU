import PublisherSalesPerRegion as PubSales
import MeanCriticScores as MeanScores
<<<<<<< HEAD
import SalesbyRegion as RegSales
=======
import dataCallum as dc
>>>>>>> c9e93fffcf93c8ea08d4f0f6efcedf0b3fee2e7c

def main_menu():
    print("--MENU--")
    print("1. Display Mean Critic score for each genre")
    print("2. Display 10 highest critically scored games")
    print("3. Display top 5 selling publishers per region")
    print("4. Display regions with most games sold")
    print("5. Option 5")
    print("6. Exit")

loop=True

while loop:
    main_menu()
    choice = int(input("Enter your choice [1-6]: "))
    if choice==1:
        #Dom's Code
        loop=False
        MeanScores.MeanCriticScores()
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
        print("Option 5 Selected")
        loop=False
    elif choice==6:
        print ("Exiting...")
        loop=False
    else:
        print("Invalid selection!")

print ("Exiting...")
	