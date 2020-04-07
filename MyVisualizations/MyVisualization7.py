'''
 This is to plot the cumulative Graphs to compare the Data Accross Various Countries

'''


# to get the data of required country
from DataSupply import Supply

#  graphical Data visulaization library for ploting sub plots
from plotly.subplots import make_subplots
import plotly.graph_objects as go


try:
    db_India = Supply('India')
    db_Korea = Supply('South Korea')
    db_China = Supply('China')

except:
    print('Not able to get data')

fig = make_subplots( rows =  2, cols = 2,
    subplot_titles= ('China', 'South Korea', 'India'),
    specs= [
               [     {},          {}  ],
               [ {'colspan': 2}, None]
           ]
        )


fig.add_trace(go.Bar(x = db_China['Date'], y = db_China['Confirmed'],
                    marker = dict(color = db_China['Confirmed'], coloraxis = 'coloraxis')), 1,1)

fig.add_trace(go.Bar(x = db_Korea['Date'], y = db_Korea['Confirmed'],
                    marker = dict(color = db_Korea['Confirmed'], coloraxis = 'coloraxis')), 1,2)

fig.add_trace(go.Bar(x = db_India['Date'], y = db_India['Confirmed'],
                    marker = dict(color = db_India['Confirmed'], coloraxis = 'coloraxis')), 2,1)

fig.update_layout(coloraxis = dict(colorscale = 'Bluered_r'), showlegend = False,
                 title_text = 'Total Confirmed Cases ',
                 plot_bgcolor = 'rgb(230,230,230)' )

fig.show()  #renders the graph in default browser


