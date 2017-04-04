#python script to work with csv data
#to run: python trackTimes.py

#fakeData1.csv can be used for testing purposes
#actual data used for this is private, ask a CAPTAIN collaborator for the info.
#the actual data has the columns: run, event, track, plane, hits, wireStart, wireStop, timeStart, timeStop, comments, author

#here, "hits" are ones identified via so-called hand-scanning of event displays showing calibrated hit charge
#a single hit is a hit of any charge > 0 in one of the three planes

#Jieun Yoo, last updated April 4, 2016


#!/usr/bin/env/python
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

blue, = sns.color_palette("muted",1)

df = pd.read_table('fakeData1.csv',sep=',')
print df

#For each 1-D track in 1 plane, calculate the length in time of the track (ie.., stopTime-startTime)
#actually, i'll take the absolute value in case someone switched data during data entry
def timeplot1():
	df2 = (df['timeStop'] - df['timeStart']).abs()
	timefig1=plt.figure()
	plt.hist(df2)
	plt.title("Duration of every 1-D track")
	plt.xlabel("time (microseconds)")
	plt.ylabel("number of events")
	timefig1.savefig('timeplot1.png')
	#plt.show()
	count = df2.count()
	std = df2.std()
	se = std/math.sqrt(count)
	print df2.describe()
	print se

#Same as above, but separate them into 3 plots, one for each plane (U,V,X)
def timeplot2():
	df['time'] = (df['timeStop'] - df['timeStart']).abs()
	#timegrouped=df['time'].groupby([df['run'],df['event'],df['track'],df['plane']])
	timegrouped=df['time'].groupby([df['plane']])
	uArray = []
	vArray = []
	xArray = []
	for name,group in timegrouped:
		if name == 'u' or name == 'U':
			uArray.append(group)
		if name == 'v' or name == 'V':
			vArray.append(group)
		if name == 'x' or name == 'X':
			xArray.append(group)

	timeUplane=plt.figure()
	plt.hist(uArray)
	plt.title("Duration of each 1-D track in the U plane")
	plt.xlabel("time (microseconds)")
	plt.ylabel("number of events")
	timeUplane.savefig('timeUplane.png')

	timeVplane=plt.figure()
	plt.hist(vArray)
	plt.title("Duration of each 1-D track in the V plane")
	plt.xlabel("time (microseconds)")
	plt.ylabel("number of events")
	timeVplane.savefig('timeVplane.png')

	timeXplane=plt.figure()
	plt.hist(xArray)
	plt.title("Duration of each 1-D track in the X plane")
	plt.xlabel("time (microseconds)")
	plt.ylabel("number of events")
	timeXplane.savefig('timeXplane.png')
	plt.show()

#until the V plane bug is fixed, we need to ignore the V plane data 
#timeplot3 is added to plot a stacked histogram of just the U or X planes
def timeplot3():
	df['time'] = (df['timeStop'] - df['timeStart']).abs()
	#timegrouped=df['time'].groupby([df['run'],df['event'],df['track'],df['plane']])
	timegrouped=df['time'].groupby([df['plane']])
	uxArray = []
	for name,group in timegrouped:
		if name == 'u' or name == 'U' or name == 'x' or name == 'X':
			uxArray.append(group)

	timeUXplane=plt.figure()
	plt.hist(uxArray,color=['royalBlue', 'Khaki'],label=['U plane','X plane'],stacked=True)
	plt.title("Duration of each 1-D track in the U or X planes")
	plt.xlabel("time (microseconds)")
	plt.ylabel("number of events")
	plt.legend()
	timeUXplane.savefig('timeUXplane.png')
	plt.show()


#MAIN
def main():
	timeplot1()
	timeplot2()
	timeplot3()

if __name__ == "__main__":
	main()
