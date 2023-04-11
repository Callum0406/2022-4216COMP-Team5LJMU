import pandas as pd
import matplotlib.pyplot as matplot
#import necessary packages

data = pd.read_csv("Tagged-Data-Final.csv")
#import data from excel file

def optionMenu():
    print("Select an option")
    print("")
    print("1) Top ten critically scored games")
    print("2) Lowest ten critically scored games")

    while True:

        criticSCselection = input("Enter a choice: ")

        if(criticSCselection == "1"):
            extracted_data = data.sort_values("Critic_Score", ascending=False).head(10)
             #shows data descending 
            name = extracted_data.Name
            criticsc = extracted_data.Critic_Score

            matplot.bar(name, criticsc)
            matplot.title("Top Ten Games By Critic Score")

            matplot.xlabel("Name")
            matplot.ylabel("Critic Score")
            #axis labels
            matplot.show()
            #produces bar chart
            break
        elif(criticSCselection == "2"):
            extracted_data = data.sort_values("Critic_Score", ascending=True).head(10)
             #shows data descending 
            name = extracted_data.Name
            criticsc = extracted_data.Critic_Score

            matplot.bar(name, criticsc)
            matplot.title("Ten Lowest Games By Critic Score")

            matplot.xlabel("Name")
            matplot.ylabel("Critic Score")
            #axis labels
            matplot.show()
            #produces bar chart
            break
        else:
            print("Please enter 1 or 2")
            print("")
            optionMenu()    





    
   