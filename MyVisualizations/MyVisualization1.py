'''
  This visualizations deals with the data of India
  which has States Name, Number of Deaths, Cured,
  Total Confirmed Cases(Indian National)
  Total Confirmed Cases (Foreign National)
'''


import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
#import seaborn as sns

df_India = pd.read_excel('../Data_contents/Covid cases in India.xlsx')

df_India.drop(['S. No.'], axis = 1, inplace = True)

# method to get total Number of Confirmed Cases
def TotalCC():
    df_India['Total confirmed Cases'] = df_India['Total Confirmed cases (Indian National)'] + df_India['Total Confirmed cases ( Foreign National )']
    # print(df_India['Total confirmed Cases'])
    total_confirmed_cases = df_India['Total confirmed Cases'].sum()
    print('Total Confirmed Cases',total_confirmed_cases)
    return total_confirmed_cases


def print_headers():
    '''' print(df_India.columns.values) this is to print the headers list this can
    done with  print(list(df_India)) '''
    print(list(df_India))

# method to get Total Number of active cases
def TotalAC():
    df_India['Active Cases'] = TotalCC() - (df_India['Death'] + df_India['Cured'])
    total_active_cases = df_India['Active Cases'].sum()
    print('total_active_cases: ',total_active_cases )
    return total_active_cases


