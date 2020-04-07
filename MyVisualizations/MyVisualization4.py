'''
 In this visualization we compare India with other countries
 in respective data of each country and predict the covid outburst
 in India

 This visualization is mainly on the Death cases accross the world

'''

# data visualization library
import pandas as  pd

# graphical visualization libraries
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
import plotly.express as px
#import seaborn as sns
import plotly.graph_objects as go

import numpy as np

#import to handle warning
import warnings
warnings.filterwarnings('ignore')


df_world_death = pd.read_csv('../Data_contents/time_series_covid19_deaths_global.csv')
df_world_death.drop( ['Province/State', 'Lat', 'Long'], axis = 1, inplace = True )

def print_header():
    '''' print(df_India.columns.values) this is to print the headers list this can
    done with  print(list(df_India)) '''
    print(list(df_world_death))


def graphVisualizationDeath(date):
    '''
    graphical visualization library used => plotly.express
    date is obtained from user
    '''
    global df_world_death
    df_world_death.sort_values(by = date, ascending = False, inplace = True)

    fig = px.bar(df_world_death, x='Country/Region',
                y = date, barmode = 'group', height = 600, color = date)

    fig.update_layout(title_text = f'Visualization of Death Cases on {date}')

    #fig = px.colors.sequential.swatches() renders color choosing site
    fig.show()  #renders the graph in default browser
    pass


if __name__ == "__main__":
    counter = True
    while(counter):
        date = input("Enter the Date : ")
        month= input("Enter the Month : ")
        input_data = month + '/' + date + '/' + '20' #formating to required format
        try:
            graphVisualizationDeath(input_data)
        except:
            print('Invalid Date')
        finally:
            if( input('Press q to Quit : ') == 'q' ):
                print('Terminating ..')
                counter = False
            else:
                pass










