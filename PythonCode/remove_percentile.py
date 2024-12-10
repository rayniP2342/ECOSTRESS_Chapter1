import arcpy
from arcpy.sa import *
import numpy as np
import os

# Define folder with raster files and output folder
in_folder = "E:/ECOSTRESS/AZ_HUC8/AmeriFlux/Sites/TIFFS"
out_folder = "E:/ECOSTRESS/AZ_HUC8/AmeriFlux/Sites/FilteredTIFFS"

arcpy.env.workspace = in_folder
arcpy.env.overwriteOutput = True

# Set threshold for percentile ( 95 = removes values above 95% percentile )
thresh = 95

try:
    # Check if the Spatial Analyst extension is available
    if arcpy.CheckExtension("Spatial") == "Available":

        # Check out the Spatial Analyst extension
        arcpy.CheckOutExtension("Spatial")

        # Make list of raster files
        rast_list = arcpy.ListRasters("*", "TIF")

        # Function to calculate mean and standard deviation of raster band
        # Ignore NaN values
        def calc_stats(rast_band):
            arr = arcpy.RasterToNumPyArray(rast_band, nodata_to_value=np.nan)
            mean = np.nanmean(arr)
            stdev = np.nanstd(arr)
            min_val = np.nanmin(arr)
            max_val = np.nanmax(arr)
            return mean, stdev, min_val, max_val

        # Function to calculate percentile of raster band
        def calc_perc(rast_band):
            arr = arcpy.RasterToNumPyArray(rast_band, nodata_to_value=np.nan)
            percentile = np.nanpercentile(arr, thresh)
            return percentile

        # Iterate through raster files
        for rast_file in rast_list:
            in_rast = arcpy.Raster(os.path.join(in_folder, rast_file))
            band_count = in_rast.bandCount
            print("{} : number of bands = {}".format(rast_file, band_count))

            # Make empty out band list
            out_bands = []
            for band_index in range(1, band_count + 1):
                band = arcpy.Raster(os.path.join(in_folder, rast_file) + "/Band_{0}".format(band_index))

                # Calculate min/max/mean/stdev for each band
                percentile = calc_perc(band)
                print("Band {0}: {1} Percentile = {2:2.2f}".format(band_index, thresh, percentile))

                # Make conditional raster to replace outliers
                out_band = SetNull((band > percentile), band)
                out_bands.append(out_band)
                print("Band {0} values greater than {1} percentile removed".format(band_index, thresh))

            # Merge bands back together
            out_rast = arcpy.management.CompositeBands(out_bands)

            # Construct output raster path
            out_name = os.path.join(out_folder, rast_file)
            out_name_perc = out_name.replace(".tif", "_p95filt.tif")
            arcpy.management.CopyRaster(out_rast, out_name_perc)
            print("{0} cleaned and saved to {1}".format(rast_file, out_folder))

            #create text file to store new stats
            filename = out_name_perc[:-4]
            fileout = filename + "_stats.txt"
            fout = open(fileout, "w")
            fout.write("{0:<6} {1:<6} {2:<6} {3:<6} {4:<6}\n".format("Band", "Min", "Max", "Mean", "Stdev"))
            
            # Define new bands
            clean_rast = arcpy.Raster(out_name_perc)
            band_count2 = clean_rast.bandCount
            for band_index2 in range(1, band_count2 + 1):
                band2 = arcpy.Raster(out_name_perc + "/Band_{0}".format(band_index2))

                # Re-calculate statistics
                mean, stdev, min_val, max_val = calc_stats(band2)

                # Write stats to text file
                fout.write("{0:<6} {1:<6.2f} {2:<6.2f} {3:<6.2f} {4:<6.2f}\n".format(band_index2, min_val, max_val, mean, stdev))

            fout.close()

        # Check in the Spatial Analyst extension
        arcpy.CheckInExtension("Spatial")

    else:
        raise RuntimeError("Spatial Analyst extension is not available.")

except arcpy.ExecuteError:
    print("Geoprocessing error:")
    print(arcpy.GetMessages(2))

except Exception as e:
    print("General error:")
    print(e)
