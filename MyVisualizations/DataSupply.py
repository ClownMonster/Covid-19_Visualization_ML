'''

 This Returns the data of required Country with Confirmed , Death  and Recovered Cases

'''


import pandas as pd

df = pd.read_csv('../Data_contents/covid_19_clean_complete.csv') # Complete Global Data Frame
df.drop(['Province/State', 'Lat', 'Long'], axis = 1, inplace = True)

def Supply(CountryName):
    global df
    db_returned = df[ df['Country/Region'] == CountryName] # Data Frame of required Country
    db_returned = db_returned[ db_returned['Confirmed'] > 0.0 ] # Data Frame with CC > 0 for Optimization
    print(db_returned)
    return db_returned


