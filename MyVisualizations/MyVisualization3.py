'''
 In this visualization we compare India with other countries
 in respective data of each country and predict the covid outburst
 in India

 This visualization is mainly on the Confirmed cases accross the world

'''

# data visualization library
import pandas as  pd

# graphical visualization libraries
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go

import numpy as np

#import to handle warning
import warnings
warnings.filterwarnings('ignore')


df_world = pd.read_csv('../Data_contents/time_series_covid19_confirmed_global.csv')
df_world.drop( ['Province/State', 'Lat', 'Long'], axis = 1, inplace = True )

def print_header():
    '''' print(df_India.columns.values) this is to print the headers list this can
    done with  print(list(df_India)) '''
    print(list(df_world))


df_world.sort_values(by = '3/21/20', ascending = False, inplace = True)


date = '3/21/20'
fig = px.bar(df_world, x='Country/Region',
             y = date, barmode = 'group', height = 600, color = date
             )
fig.update_layout(title_text = f'Visualization of Confirmed Cases on {date}')

#fig = px.colors.sequential.swatches() renders color choosing site
fig.show()