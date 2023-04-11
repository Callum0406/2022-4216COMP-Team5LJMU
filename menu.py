import GenrePieChartData as PieData
#import PublisherSalesPerRegion as PubSales
#import MeanCriticScores as MeanScores
#import SalesbyRegion as RegSales
#import dataCallum as dc

def main_menu():
    print("--MENU--")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Display sales by genre")
    print("6. Exit")

loop=True

while loop:
    main_menu()
    choice = int(input("Enter your choice [1-6]: "))
    
    if choice==1:
        print ("Option 1 Selected")
        loop=False
    elif choice==2:
        print ("Option 2 Selected")
        loop=False
    elif choice==3:
        print ("Option 3 Selected")
        loop=False
    elif choice==4:
        print ("Option 4 Selected")
        loop=False
    elif choice==5:
        print("Option 5 Selected")

    elif choice==6:
        print ("Exiting...")
        loop=False
    else:
        print("Invalid selection!")
