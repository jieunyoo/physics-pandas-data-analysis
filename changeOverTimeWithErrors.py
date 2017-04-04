import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#hard-coded data - each "Set" has a different physical run configuation
Day_Set0 = [2]
Day_Set1 = [5]
Day_Set2 = [5,15,18]

Mean_Set0 = [24.78]
Mean_Set1 = [21.33]
Mean_Set2 = [24.27,30.61,27.71]

StandardError_Set0 = [7.16]
StandardError_Set1 = [1.8]
StandardError_Set2 = [2.77,0.98,1.18]

RunNumber_Set0 = [6144]
RunNumber_Set1 = [6300]
RunNumber_Set2= [6301,6338,6377]


#plot data
fig,ax = plt.subplots()

ax.scatter(Day_Set0,Mean_Set0, label = "set 0", marker="+",color="green")
ax.errorbar(Day_Set0,Mean_Set0,yerr=StandardError_Set0,linestyle="None", color="green")
for i, txt in enumerate(RunNumber_Set0):
	ax.annotate(txt,(Day_Set0[i],Mean_Set0[i]))

ax.scatter(Day_Set1,Mean_Set1, label = "set1", marker="+",color="red")
ax.errorbar(Day_Set1,Mean_Set1,yerr=StandardError_Set1,linestyle="None", color="red")
for i, txt in enumerate(RunNumber_Set1):
	ax.annotate(txt,(Day_Set1[i],Mean_Set1[i]))

ax.scatter(Day_Set2,Mean_Set2, label = "set2", marker="+")
ax.errorbar(Day_Set2,Mean_Set2,yerr=StandardError_Set2,linestyle="None")
for i, txt in enumerate(RunNumber_Set2):
	ax.annotate(txt,(Day_Set2[i],Mean_Set2[i]))

#labels, legend, etc.
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.tick_params(axis='both',which='minor',labelsize=15)

plt.xlabel("Number of days since start of run")
plt.ylabel("Avg. length of tracks (microseconds)")
plt.title("Duration of tracks")
plt.legend(loc='lower right')
plt.show()
