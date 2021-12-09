import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go

labels = ['Yellow','Red','Green']
values = [4500, 2500, 1053]
colors = ['Yellow', 'Red', 'Green']

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
marker=dict(colors=colors)
fig.write_html("graph.html")