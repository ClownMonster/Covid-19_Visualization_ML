'''
    This is just to renders the graphs for Confirmed, Death and Recovered Cases
    simultaneously on a day globally

'''

from MyVisualization3 import graphVisualizationConfirmed
from MyVisualization4 import graphVisualizationDeath
from MyVisualization5 import graphVisualizationRecovered


if __name__ == "__main__":
    counter = True
    while(counter):
        date = input("Enter the Date : ")
        month= input("Enter the Month : ")
        input_data = month + '/' + date + '/' + '20' #formating to required format
        try:
            graphVisualizationConfirmed(input_data)
            graphVisualizationDeath(input_data)
            graphVisualizationRecovered(input_data)
        except:
            print('Invalid Date')
        finally:
            if( input('Press q to Quit : ') == 'q' ):
                print('Terminating ..')
                counter = False
            else:
                pass