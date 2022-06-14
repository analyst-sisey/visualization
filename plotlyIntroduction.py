# Creating a simple bar chart using plotly
# In this simple exmples, we will input or data directly into our code

import plotly.express as px

fig = px.bar(    
x= ["Crude Oil", "Grains", "Pharmaceuticals","Furniture"],
y= [50, 58, 70, 35]
)
# write the diagram to an html file
fig.write_html('bar_plot.html', auto_open=True)


# # Below is another example to create a scatter plot using plotly. Remove comments and run

# fig = px.scatter( 
#     x =[1,20,5,12,30,25,50] ,
#     y = [50,5,12,30,15,25,20]
#     )

# fig.write_html('scatter.html', auto_open=True)
