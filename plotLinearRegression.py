'''
script to do a simple linear regression on data contained in fakeData.dat
to run, python linearRegressionData.py
'''

#!/usr/bin/env/python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

#read in file data.dat, which has 3 columns, day:length:yerrors
data = np.loadtxt('fakeDataForLinearRegressionPlot.dat')
a = data[:,0]
b = data[:,1]
errors = data[:,2]

#very simple linear regression
X = sm.add_constant(a)
sm_model = sm.OLS(b,X)
estimate= sm_model.fit()
print estimate.summary()

#(y-intercept,slope)
print estimate.params

#original data
plt.scatter(a,b, label = "data", marker="+")
plt.errorbar(a,b,yerr=errors,linestyle="None")

#linear regression line, will be fit to min. and max values of array a
X_prime = np.linspace(a.min(),a.max(),100)[:,np.newaxis]
X_prime = sm.add_constant(X_prime)
y_hat = estimate.predict(X_prime)
plt.plot(X_prime[:,1],y_hat,'r')

plt.xlabel("days since start of neutron run")
plt.ylabel("avg. length of tracks (microseconds)")
plt.title("Duration of tracks")
plt.legend(loc='lower right')
plt.show()
