__author__ = 'leilu'

from sklearn import linear_model
from statsmodels.formula.api import ols
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from data_clean import *
import statsmodels.formula.api as smf
import math



data = pd.read_csv("NYPD_Motor_Vehicle_Collisions.csv", header=0, sep=',')
df = pd.DataFrame(data)
df = dataCleanForRegression(df)

"""
Multiple Regression
"""

msk = np.random.rand(len(df)) < 0.75
train = df[msk]
test = df[~msk]


ols = sm.OLS(train['Number of total People injured and killed'], train.drop('Number of total People injured and killed', 1))
result = ols.fit()

print result.summary()

""""
OLS Linear Regression Model
"""""

Y = df['Number of total People injured and killed']  # response
X = df['num_vehicles_involved']  # predictor
X = sm.add_constant(X) # Adds a constant term to the predictor

est = sm.OLS(Y, X)
est = est.fit()
print est.params

X_prime = np.linspace(X['num_vehicles_involved'].min(), X['num_vehicles_involved'].max(), 5)[:, np.newaxis]
X_prime = sm.add_constant(X_prime)  # add constant as we did before

plt.ylim([0, 35])
y_hat = est.predict(X_prime)
plt.scatter(X['num_vehicles_involved'], Y, alpha=0.3)  # Plot the raw data
plt.xlabel("Number of Vehicles")
plt.ylabel("Total Fatalities")
plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9) #plot regession line
plt.show()