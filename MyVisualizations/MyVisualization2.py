'''
This visualization Deals with the Entire data of the globe
includes countries name, latitute and longitude,
@ Respective Dates Total number of Confirmed , Deaths, Recovered Cases

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

df_full = pd.read_csv('../Data_contents/covid_19_clean_complete.csv')
df_full.drop(['Province/State'], axis = 1, inplace = True)

def print_header():
    '''' print(df_India.columns.values) this is to print the headers list this can
    done with  print(list(df_India)) '''
    print(list(df_full))




'''
    Now we have Visualization Over Geographical locations
    by rendering Graphs
'''

def Date_vs_CC():

    '''
        This graphs plots the Date againts the Confirmed cases
        on each  day.
        plotly.graph_object is used for graphical visualization here  with Scatter Graph

    '''

    fig = go.Figure()

    fig.add_trace( go.Scatter(x = df_full['Date'],
                            y = df_full['Confirmed'],
                            mode = 'lines+markers',
                            name = 'Total Cases' ) )


    fig.update_layout(title_text = "Clown Monster's Visualization",
                      plot_bgcolor = 'rgb(230,230,230)')

    fig.show() # renders the graph in default browser



def Date_vs_Deaths():

    '''
        This graphs plots the Date againts the Death Cases
        on each  day.
        plotly.graph_object is used for graphical visualization here  with Scatter Graph

    '''

    fig = go.Figure()

    fig.add_trace( go.Scatter(x = df_full['Date'],
                            y = df_full['Deaths'],
                            mode = 'lines+markers',
                            name = 'Total Deaths' ) )


    fig.update_layout(title_text = "Clown Monster's Visualization",
                      plot_bgcolor = 'rgb(230,230,230)')

    fig.show() # renders the graph in default browser




def Date_vs_Recovered():

    '''
        This graphs plots the Date againts the Recovered cases
        on each  day.
        plotly.graph_object is used for graphical visualization here with Scatter Graph

    '''

    fig = go.Figure()

    fig.add_trace( go.Scatter(x = df_full['Date'],
                            y = df_full['Recovered'],
                            mode = 'lines+markers',
                            name = 'Total Recovered' ) )


    fig.update_layout(title_text = "Clown Monster's Visualization",
                      plot_bgcolor = 'rgb(230,230,230)')

    fig.show() # renders the graph in default browser





