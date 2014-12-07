'''
Created on Dec 2, 2014

@author: luchristopher
'''
from ioprocess import *


def main():
    dataframe_reader = DataReader()
    raw_data=dataframe_reader.safeReadCsvLocal('./data/NYPD_Motor_Vehicle_Collisions.csv')
    
    

if __name__ == '__main__':
    main()