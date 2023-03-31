import PublisherSalesPerRegion as PubSales

def main_menu():
    print("--MENU--")
    print("1. Option 1")
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
        loops=False
    elif choice==2:
        print ("Option 2 Selected")
        loop=False
    elif choice==3:
        publisherSalesLoop = True
        publisherRegionChoice = 0
        while publisherSalesLoop:
            print("Select the region to display.")
            print("1. North America")
            print("2. Europe")
            publisherSalesChoice = int(input())
            if publisherSalesChoice==1:
                PubSales.top5PublisherSales("NA_Sales")
            elif publisherSalesChoice==2:
                PubSales.top5PublisherSales("EU_Sales")
            else:
                print("Error: Invalid Option")
                quit()
        loop=False
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
	