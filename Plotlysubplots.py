
# Plotly Express does not support arbitrary subplot capabilities.
# The lower-level plotly.subplots module and the make_subplots function 
# it exposes are used to construct figures with arbitrary subplots. 
# This allows users to plot various figures on a single page. This is very useful for creating dashboards.


from plotly.subplots import make_subplots
import plotly.graph_objects as pg
import pandas as pd


# The make_subplots() is used to define the number of rows and columns.
fig = make_subplots(rows=1, cols=4,column_widths=[0.5, 0.5,0.5, 0.5])

fig.add_trace(
    pg.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    # pg.bar(df, x ='Year' , y = 'Average Rainfall'),
    
        
    row=1, col=1
)
fig.add_trace(
    
    pg.Bar(x=[1, 2, 3], y=[4, 5, 6]),
        
    row=1, col=2
)
fig.add_trace(
    pg.Scatter(x=[1, 2, 3], y=[4, 5, 6]),

        
    row=1, col=3
)
fig.add_trace(
    pg.Bar(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=4
)
# Controlling the page wdith and height
# fig.update_layout(height=600, width=1300, title_text="Side By Side Subplots")
fig.show()
