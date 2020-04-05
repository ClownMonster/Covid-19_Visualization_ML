'''
  This visualizations deals with the data of India
  which has States Name, Number of Deaths, Cured,
  Total Confirmed Cases(Indian National)
  Total Confirmed Cases (Foreign National)

  TC = Total Confirmed Cases
  AC = Total Active Cases
  C = Cured
  D = Deaths

'''

import pandas as pd


import numpy as np

# graphical visualization libraries
import matplotlib
matplotlib.use('Agg')
''' important to render the graphs if

removed we get  Segmentation fault (core dumped)

'''
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

# visualization with maps
#import folium
#from folium import plugins

#import to handle warnings
import warnings
warnings.filterwarnings('ignore')


df_India = pd.read_excel('../Data_contents/Covid cases in India.xlsx')

df_India.drop(['S. No.'], axis = 1, inplace = True)

# method to get total Number of Confirmed Cases
def TotalCC():
    global df_India
    df_India['Total confirmed Cases'] = df_India['Total Confirmed cases (Indian National)'] + df_India['Total Confirmed cases ( Foreign National )']
    # print(df_India['Total confirmed Cases'])
    total_confirmed_cases = df_India['Total confirmed Cases'].sum()
    print('Total Confirmed Cases : ',total_confirmed_cases)
    return total_confirmed_cases


def print_headers():
    '''' print(df_India.columns.values) this is to print the headers list this can
    done with  print(list(df_India)) '''
    print(list(df_India))

# method to get Total Number of active cases
def TotalAC():
    global df_India
    df_India['Active Cases'] = df_India['Total confirmed Cases'] - (df_India['Death'] + df_India['Cured'])
    total_active_cases = df_India['Active Cases'].sum()
    print('total_active_cases: ',total_active_cases )
    return total_active_cases



# method to get the Active Cases data of Each state in decending order
def OrdererdAC():
    TotalCC()
    TotalAC()
    total_cases = df_India.groupby('Name of State / UT')['Active Cases'].sum().sort_values(ascending = False).to_frame()
    print(total_cases)


TotalCC()
TotalAC()

'''
    Now we have Visualization Over Geographical Maps
    by rendering Graphs

 '''

def TC_vs_C_D():
    '''
    This Method renders the graph using seaborn
    The graph shows the relationship between Each states Total cofirmed Cases,
    Cured and Deaths.

    Cured is given Green color in the Graph
    Deaths is given Red Color in the Graph

    '''
    fig, ax  =  plt.subplots()
    data = df_India[['Name of State / UT', 'Total confirmed Cases', 'Cured', 'Death']]
    data.sort_values('Total confirmed Cases', ascending = False, inplace = True)

    sns.set_color_codes('pastel')
    sns.barplot(x = 'Total confirmed Cases', y = 'Name of State / UT',
                color= 'r', data = data, label = 'Total Cases')

    sns.set_color_codes('muted')
    sns.barplot(x='Cured',y='Name of State / UT', color='g', label='Cured', data = data )

    fig.savefig('./v1.eps', format='eps') # saving the graph to the current folder with eps format

