'''
    Here Scatter Graph is used for graphical Visualization of India
    having Confirmed, Death and Recovered Data

'''


# imports to get the Data of Confirmed, Death, Recovered Cases  accross the globe
from DataSupply import Supply


# graphical visualization libraries
import plotly.graph_objects as go
import plotly.express as px


df_India = Supply('India')


fig = go.Figure()

fig.add_trace(go.Scatter( x = df_India['Date'], y = df_India['Confirmed'],
                         mode = 'lines+markers', name = 'Confirmed', line = dict(color = 'Green') ))


fig.add_trace(go.Scatter( x = df_India['Date'], y = df_India['Deaths'],
                         mode = 'lines+markers', name = 'Deaths', line = dict(color = 'Red') ))


fig.add_trace(go.Scatter( x = df_India['Date'], y = df_India['Recovered'],
                         mode = 'lines+markers', name = 'Recovered', line = dict(color = 'Blue') ))


fig.update_layout(title_text = "Visualization of Indian Data", yaxis = dict(title = "Number of Cases"))
fig.show()



