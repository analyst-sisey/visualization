# Reading data from a csv file and visualizing the data using plotly
# The csv file contains the weather data for Ghana

import plotly.express as px

# we will use pandas to read the csv file and load it into plotly
import pandas as pd

# Read the csv file. Please make sure the file path matches your csv file location. 
df = pd.read_csv('Weather.csv')

# You can change the chart type using the px.chartType method.
#  For EXAMPLE px.line() for line graph or px.scatter() for scatter plot
fig = px.bar(df, 
x ='Year' , 
y = 'Average Rainfall'
)

fig.show()

# Below is another example to create a stacked bar chart using plotly. Remove comments and run

# fig = px.bar(df, x ='Year' , y = ['Average Rainfall', 'Average Min Temp', 'Average Max Temp'], title= 'Weather Data')

# fig.show()

