import arcpy
from arcpy.sa import *
import numpy as np
import os

# Define folder with raster files and output folder
in_folder = "K:/Rayni_Lewis/AmeriFlux/ECOSTRESS/500m"
out_folder = "K:/Rayni_Lewis/AmeriFlux/ECOSTRESS/500m"

arcpy.env.workspace = in_folder
arcpy.env.overwriteOutput = True

# Function to calculate mean and standard deviation of raster band
def calc_stats(rast_band):
    arr = arcpy.RasterToNumPyArray(rast_band, nodata_to_value=np.nan)
    mean = np.nanmean(arr)
    stdev = np.nanstd(arr)
    min_val = np.nanmin(arr)
    max_val = np.nanmax(arr)
    return mean, stdev, min_val, max_val


# Make list of raster files
rast_list = arcpy.ListRasters("*", "TIF")

# Iterate through raster files
for rast in rast_list:
    in_rast = arcpy.Raster(os.path.join(in_folder, rast))
    band_count = in_rast.bandCount

    filename = rast[:-4]
    fileout = out_folder + "/" + filename + "_basicstats.txt"
    fout = open(fileout, "w")
    fout.write("{0:<6} {1:<6} {2:<6} {3:<6} {4:<6}\n".format("Band", "Min", "Max", "Mean", "Stdev"))


    # Iterate through bands
    for band_index in range(1, band_count + 1):
        band = arcpy.Raster(os.path.join(in_folder, rast) + "/Band_{0}".format(band_index))

        # Calculate stats for each band
        mean, stdev, min_val, max_val = calc_stats(band)

        # Write stats to text file
        fout.write("{0:<6} {1:<6.2f} {2:<6.2f} {3:<6.2f} {4:<6.2f}\n".format(band_index, min_val, max_val, mean, stdev))

    fout.close()
        
