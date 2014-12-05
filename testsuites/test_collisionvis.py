'''
Created on Dec 3, 2014

@author: luchristopher
'''
import unittest
from collisionvis import *
from ioprocess import *
import time


class TestCollisionVisualizer(unittest.TestCase):


    def setUp(self):
        self.test_data_reader = DataReader()
        self.test_object = CollisionVisualizer(self.test_data_reader.safeReadCsvLocal('../data/NYPD_Motor_Vehicle_Collisions.csv'))


    def tearDown(self):
        pass


#     def test_getVehicleTypes(self):
#         print self.test_object._getVehicleTypes()
        
    def test_pieChartVehicleTypes(self):
        self.test_object.pieChartVehicleTypes()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()