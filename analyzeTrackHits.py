#python script to work with csv data
#to run: python analyzeTrackHits.py

#fakeData1.csv can be used for testing purposes
#fakeData1.csv is a csv file with the following headings: run,event,track,plane,hits,timeStart,timeStop

#actual data used for this is private, ask a CAPTAIN collaborator for the info.
#the actual data has the columns: run, event, track, plane, hits, wireStart, wireStop, timeStart, timeStop, comments, author

#here, "hits" are ones identified via so-called hand-scanning of event displays showing calibrated hit charge
#a single hit is a hit of any charge > 0 in one of the three planes

#Jieun Yoo, last updated March 13, 2016


#!/usr/bin/env/python
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

blue, = sns.color_palette("muted",1)

df = pd.read_table('fakeData1.csv',sep=',')
print (df)
	
#For one run, for each event, plot the total number of hits in all planes (U+V+X) in all tracks 
def plot1():	
	grouped=df['hits'].groupby([df['run'],df['event']])
	df1 = grouped.aggregate(np.sum)
	print (df1)
	df1.to_csv('plot1.csv')
	x,y = np.loadtxt('plot1.csv',delimiter=',',usecols=(1,2),unpack=True)
	fig1 = plt.figure()
	plt.scatter(x,y)
	plt.title("Number of hits in all planes (U+V+X) in all tracks / event")
	plt.ylabel("number of hits in all planes (U+V+X) in all tracks")
	plt.xlabel("event number")
	fig1.savefig('plot1.png')
	plt.show()

#For one run, for each event, for each track, histogram the total number of hits in all planes(U+V+X)
def plot2():
	grouped2=df['hits'].groupby([df['run'],df['event'],df['track']])
	df2 = grouped2.aggregate(np.sum)
	print (df2)
	df2.to_csv('plot2.csv')
	df2=pd.read_table('plot2.csv',sep=',',header=None)
	df2['index_col'] = df2.index
	df2.columns=['run', 'event', 'track','hits','index']
	print (df2)
	fig2 = plt.figure()
	plt.hist(df2['hits'])
	plt.title("Number of hits in all planes (U+V+X) per single track")
	plt.xlabel("number of hits in all planes per single track")
	plt.ylabel("number of events")
	fig2.savefig('plot2.png')
	plt.show()


#For one run, for each track in an event, plot the frequency of combinations of planes hit
#here, a single 'track' can be distinguished from another by having a different overall timing from the other track
def plot3():
	grouped3=df['plane'].groupby([df['run'],df['event'],df['track']])
	df3 = grouped3.agg(lambda x: ''.join(set(x)))
	df3.to_csv('plot3.csv')
	df3=pd.read_table('plot3.csv',sep=',',header=None)
	df3['index_col'] = df3.index
	df3.columns=['run', 'event', 'track','plane','index']
	print (df3)
	fig3 = plt.figure()
	df3["plane"].value_counts().plot(kind="bar")
	plt.title("Frequency of planes hit per single track")
	plt.xlabel("planes hit by a single track")
	#plt.xlabel("planes hit by a single track", size = 20)
	plt.ylabel("number of events")
	fig3.savefig('plot3.png')
	plt.show()

#For one run, for each 'track' in an event, do a simple count of how many planes were hit
#here, a 1-D 'track' is a set of hits that meet a certain threshold and that are close in time and fairly consistent in spanning wires
#for the first data pass, the threshold was 5 hits, and small gaps in wires spanned was allowed, e.g., due to poor data quality or unconnected wires
#so, a single 'track' here can be composed of any number of hits in the planes, but those hits are separated in time from another single 'track'
#In other words, here a 'track' is composed of any number of 1-D tracks at a certain time period in a certain event
def plot4():
	grouped4=df['plane'].groupby([df['run'],df['event'],df['track']])
	numberPlanesHit = []
	for name,group in grouped4:
		numberPlanesHit.append(group.size)
	fig4 = plt.figure()
	plt.hist(numberPlanesHit)
	plt.title("Number of planes hit per single track")
	plt.xlabel("Number of planes hit by a single track")
	plt.ylabel("number of events")
	fig4.savefig('plot4.png')
	plt.show()

#For one run, for each event, count how many tracks there are
#this uses the same definition of 'track' as plot4()
def plot5():
	grouped4=df['track'].groupby([df['run'],df['event']])
	numberTracksOneEvent = []
	for name,group in grouped4:
		numberTracksOneEvent.append(max(group))
	fig5 = plt.figure()
	plt.hist(numberTracksOneEvent)
	plt.title("Number of tracks in a single event")
	plt.xlabel("Number of tracks in a single event")
	plt.ylabel("number of events")
	fig5.savefig('plot5.png')
	plt.show()

#MAIN
def main():
	plot1()
	plot2()
	plot3()
	plot4()
	plot5()

if __name__ == "__main__":
	main()
