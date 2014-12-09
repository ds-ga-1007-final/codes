__author__ = 'leilu'
__author__ = 'leilu'

from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn import linear_model
from statsmodels.formula.api import ols
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from data_clean import *


data = pd.read_csv("NYPD_Motor_Vehicle_Collisions.csv", header=0, sep=',')
df = pd.DataFrame(data)
df = data_clean_for_regression(df)
'''

fatalities_boro = []
for boro in df['BOROUGH'].unique():
    observation = df4[df4['BOROUGH'] == boro]
    num_people_injured_killed = sum(observation['Number of total People injured and killed'])
    fatalities_boro.append(num_people_injured_killed)
print fatalities_boro

d = {'boro': df['BOROUGH'].unique(), 'Fatalities': map(int, fatalities_boro)}
df2 = pd.DataFrame(d)
df2 = df2.set_index('boro')
print df2

plt.figure()
ax = df2.plot(kind='bar')
plt.xlabel('boros')
plt.ylabel('Total Number of people injured or killed')
#plt.show()
'''
"""
Linear Regression
"""

print df.head()

msk = np.random.rand(len(df)) < 0.75
train = df[msk]
test = df[~msk]


ols = sm.OLS(train['Number of total People injured and killed'], train.drop('Number of total People injured and killed', 1))
result = ols.fit()

print result.summary()
