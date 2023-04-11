import pandas as pd
import matplotlib.pyplot as matplot
#import necessary packages
data = pd.read_csv("Tagged-Data-Final.csv")
#import data from excel file

print("Select and option:")
print("1. Highest Critic Scores")
print("2. Lowest Critic Scores")

loop=True

while loop:
    choice = int(input("Enter your choice 1-2: "))
    
    if choice==1:
        print ("Option 1 Selected")
        extracted_data = data.sort_values("Critic_Score", ascending=True).head(10)
        #shows data descending 
        name = extracted_data.Name
        criticsc = extracted_data.Critic_Score
        matplot.bar(name, criticsc)
        matplot.title("Ten Lowest Scored Games")

        matplot.xlabel("Name")
        matplot.ylabel("Critic Score")
        #axis labels
        matplot.show()
        #produces bar chart
        loop=False
    elif choice==2:
        print ("Option 2 Selected")
        extracted_data = data.sort_values("Critic_Score", ascending=False).head(10)
        #shows data descending 
        name = extracted_data.Name
        criticsc = extracted_data.Critic_Score

        matplot.bar(name, criticsc)
        matplot.title("Ten Highest Scored Games")

        matplot.xlabel("Name")
        matplot.ylabel("Critic Score")
        #axis labels
        matplot.show()
        #produces bar chart
        loop=False

