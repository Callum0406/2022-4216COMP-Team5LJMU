import pandas as pd
import matplotlib.pyplot as matplot
#import necessary packages
def callumData2():
    data = pd.read_csv("Tagged-Data-Final.csv")
    #import data from excel file

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