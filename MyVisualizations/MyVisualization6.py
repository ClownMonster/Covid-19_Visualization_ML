'''
 This is to Render the Graphs for Confirmed, Deaths and Recovered Cases for the Required
 Country.

'''
from DataSupply import Supply
import plotly.express as px


class clownRenders:
    def __init__(self):
        countryName = input('Enter the Country : ')
        db_ob = Supply(countryName)
        if db_ob.empty:
            print('Invalid Country Name')
            return
        else:
            self.db_ob = db_ob
            self.countryName = countryName
        return

    def forConfirmed(self):
        fig = px.bar(self.db_ob, x='Date',
                     y='Confirmed', color='Confirmed',
                      barmode='group', height=600)
        fig.update_layout(title_text = f'Visualization of Confirmed Cases in {self.countryName}')
        fig.show()
        return

    def forDeath(self):
        fig = px.bar(self.db_ob, x='Date',
                     y='Deaths', color='Deaths',
                      barmode='group', height=600)
        fig.update_layout(title_text = f'Visualization of Death Cases in {self.countryName}')
        fig.show()
        return

    def forRecovered(self):
        fig = px.bar(self.db_ob, x='Date',
                     y='Recoverd', color='Recovered',
                      barmode='group', height=600)
        fig.update_layout(title_text = f'Visualization of Recovered Cases in {self.countryName}')
        fig.show()
        return


if __name__ == "__main__":
    counter = True
    while(counter):
        ob = clownRenders() #object reference Formed for a particular country

        try:
            choice = input('1.Confirmed Cases \n2.Death Cases \n3.Recovered Cases\n4.Quit\nEnter Your Choice : ')
            if(choice == '1'):
                ob.forConfirmed()

            elif(choice == '2'):
                ob.forDeath()

            elif(choice == '3'):
                ob.forRecovered()

            elif(choice == '4'):
                counter = False

            else:
                print('Invalid Choice')

        except:
            print('Invalid Choice')






