'''
 The forecasting and  prediction is done using Prophet, an aditive models with non-linear
 trends


'''
# imports to get the Data of Confirmed, Death, Recovered Cases  accross the globe
from DataSupply import Supply

import pandas as pd
import matplotlib
matplotlib.use('Agg')

from fbprophet import Prophet

df = Supply('US')

confirmed  =  df.groupby('Date').sum()['Confirmed'].reset_index()
death = df.groupby('Date').sum()['Deaths'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()


confirmed.columns = ['ds', 'y'] # Naming the colums to send as input to prophet
confirmed['ds'] = pd.to_datetime(confirmed['ds']) # conversion from YYYY/MM/DD to YYYY-MM-DD


m = Prophet(interval_width = 0.96)
m.fit(confirmed)
future_predict = m.make_future_dataframe(periods = 20)
my_forecast =  m.predict(future_predict)
pre_data = my_forecast[[ 'ds', 'yhat', 'yhat_lower', 'yhat_upper' ] ]

fig = m.plot(my_forecast)
fig.savefig('./v2.eps', format='eps')
fig2 = m.plot_components(my_forecast)
fig2.savefig('./v3.eps', format='eps')


