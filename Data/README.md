# Data Folder

This folder contains all data needed for ECOSTRESS analysis.
It should contain:

**ECOSTRESS**

ECOSTRESS data should be in csv format. All data was extracted from stacked ECOSTRESS images in tiff format. The data was filtered by daytime image acquisitions, quaility flag, view zenith. Pixels above the 95th percentile were also removed from each image. The data was also filtered using a 250 m buffer around each AmeriFlux tower. The data file contains the columns "Band" "Min" "Max" "Mean" and "Stdev". The "Mean" column contains the mean pixel value from each buffered ECOSTRESS image. This is the column that should be used for all further analysis. 

