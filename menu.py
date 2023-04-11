import PublisherSalesPerRegion as PubSales
import GenreCriticScores as GenreScores

def main_menu():
    print("--MENU--")
    print("1. Genre Critic Scores")
    print("2. Option 2")
    print("3. Display top 5 selling publishers per region")
    print("4. Option 4")
    print("5. Option 5")
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
        print ("Option 2 Selected")
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
    elif choice==4:
        print ("Option 4 Selected")
        loop=False
    elif choice==5:
        print("Option 5 Selected")
        loop=False
    elif choice==6:
        print ("Exiting...")
        loop=False
    else:
        print("Invalid selection!")

print ("Exiting...")
	