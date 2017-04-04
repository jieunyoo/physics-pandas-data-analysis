# This repo. includes various scripts that were used for analyzing physics data from the CAPTAIN experiment.

These scripts were last modified in 2016. Note: the data format may have changed since then.

See the folder \plots for example plots

This was run with python 2.7.12, and requires both pandas and seaborn

You can run the scripts by
```
python NAME-OF-SCRIPT
```

analyzeTrackHits.py - will provide information about number of hits, tracks, planes crossed, etc.

trackTimes.py - will calculate timing information for 1D tracks

changeOverTimeWithErrors.py - will provide track information over a period of days

plotLinearRegression.py - will perform a simple linear regression on the data, and print out a summary of the stats.

Two sample fake data files are included for testing purposes.
