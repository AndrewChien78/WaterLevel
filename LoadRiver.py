# This code loads the river water level data and displays it
# It is based on an example from Jason Brownlee of Machine Learning Mastery. This code provides 
# an example of time series decomposition
# https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/
#
from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('WL_Edmonton_1day.csv', header=0)
series.plot()
pyplot.show()

