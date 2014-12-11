'''
Created on Dec 2, 2014

@author: luchristopher
'''
from dtclean import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class CollisionVisualizer():
    '''
    classdocs
    '''


    def __init__(self, init_dataframe):
        '''
        Constructor
        '''
        self._data = init_dataframe
        
    
    def _getVehicleTypes(self):
        '''
        returns the list for all vehicle type names that has been recorded in case needed, might be deleted in the next version
        ''' 
        columns_list = ['VEHICLE TYPE CODE {}'.format(x) for x in range(1,6)]
        vehicle_type_set = set()
        for type_code in columns_list:
            vehicle_type_set.update(list(self._data[type_code].dropna().unique()))
        return list(vehicle_type_set)
    
    def barGraphVehicleTypes(self,start_date=None,end_date=None):
        '''
        generate a pie chart visualizing the ratio of different types of vehicles involved in collisions within date range (start,end)
        '''
        date_ranged_data = self._data[start_date:end_date]
        record_vehicle_types = pd.Series(date_ranged_data[['VEHICLE TYPE CODE {}'.format(x) for x in range(1,6)]].values.ravel()).dropna()
        collisions_count_by_type = record_vehicle_types.value_counts()
        print collisions_count_by_type
        #plotting
        plt.style.use('ggplot')
        plt.title('Collisions By Vehicle Types, From {} to {}'.format(start_date,end_date),fontsize=12,color='k')
        plt.ylabel('Vehicle Types')
        plt.xlabel('Number of Collisions')
        collisions_count_by_type.plot(kind='barh')
        plt.tight_layout()
        plt.show()
        return collisions_count_by_type
        
        