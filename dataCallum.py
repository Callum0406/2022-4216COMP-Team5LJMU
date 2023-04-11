import pandas as pd
import matplotlib.pyplot as matplot
#import necessary packages
def dataCallum():
    data = pd.read_csv("Tagged-Data-Final.csv")
    #import data from excel file

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
    
   