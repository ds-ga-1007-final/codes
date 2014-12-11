'''
Created on Dec 2, 2014

@author: luchristopher
'''
from ioprocess import *
from dtclean import *
from collisionvis import *
from dtclean.donothing import donothingClean
from dtclean.cleanreg import dataCleanForRegression


def main():
    dataframe_reader = DataReader()
    raw_data=dataframe_reader.safeReadCsvLocal('./data/NYPD_Motor_Vehicle_Collisions.csv')
    cleaner = DataCleaner(dataCleanForRegression)
    print cleaner.clean(raw_data)
    collision_vis_demo = CollisionVisualizer(raw_data)
    

if __name__ == '__main__':
    main()