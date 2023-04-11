import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
DATA = pd.read_csv('Tagged-Data-Final.csv')

# Get the top 5 developer sales for each region
global_sales = DATA.nlargest(5, 'Global_Sales')['Global_Sales'].tolist()
na_sales = DATA.nlargest(5, 'NA_Sales')['NA_Sales'].tolist()
eu_sales = DATA.nlargest(5, 'EU_Sales')['EU_Sales'].tolist()
jp_sales = DATA.nlargest(5, 'JP_Sales')['JP_Sales'].tolist()
other_sales = DATA.nlargest(5, 'Other_Sales')['Other_Sales'].tolist()

# Labels for the x-axis and y-axis
regions = ['Global', 'North America', 'Europe', 'Japan', 'Other']
sales = 'Sales (in millions)'

# Plot the data
plt.plot(regions, global_sales, label='Global')
plt.plot(regions, na_sales, label='North America')
plt.plot(regions, eu_sales, label='Europe')
plt.plot(regions, jp_sales, label='Japan')
plt.plot(regions, other_sales, label='Other')

# Set the title and axis labels
plt.title('Top 5 Sales of Games in Different Regions')
plt.xlabel('Regions')
plt.ylabel(sales)

# Show the legend
plt.legend()

# Display the plot
plt.show()