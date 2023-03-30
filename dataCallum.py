import pandas as pd
import matplotlib as matplot
#import pandas and matplotlib for data reading and bar chart creation
data = pd.read_csv("Tagged-Data-Final.csv")
#read in file data


print("This is video games based on critic score")

x = data['Name']
y = data['Critic_Score']

plt.bar(x, y)

plt.xlabel('Game name')
plt.ylabel('Y-axis label')
plt.title('Games by user critic score')

plt.show
