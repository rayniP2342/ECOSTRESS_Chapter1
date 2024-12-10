import arcpy
import os
from os import listdir, path, mkdir

#set workspace and output folder for merged raster files
ws = "E:/ECOSTRESS/AZ_HUC8/2022/ETALEXI"
output_folder = "E:/ECOSTRESS/AZ_HUC8/2022/ETALEXI/Combined"

arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True

#create output folder if it does not exist
if not path.exists(output_folder):
    mkdir(output_folder)

#create empty list to store raster file names
raster_files = []

#iterate through files in folder and add to empty list if TIFF file
for file in listdir(ws):
    if file.endswith(".tif"):
        raster_files.append(file)

#make new empty list for filtered rasters
filtered_rasters = []

#iterate through raster list and add files with correct time to empty list
for raster_file in raster_files:
    timestamp = int(raster_file[59:61])
    if 13 <= timestamp <= 23:
        filtered_rasters.append(raster_file)
    elif 00 <= timestamp <= 1:
        filtered_rasters.append(raster_file)

#create dictionary to store raster files grouped by first 60 characters of file name
grouped_rasters = {}
for filtered_raster in filtered_rasters:
    key = filtered_raster[:61]          #get first 59 characters of file name
    if key in grouped_rasters:
        grouped_rasters[key].append(filtered_raster)
    else:
        grouped_rasters[key] = [filtered_raster]

#Iterate through the grouped raster files and perform mosiac to new raster
for key, files_list in grouped_rasters.items():
    if len(files_list) >= 2:
        name = key[41:63]
        output_mosaic = f'ALEXI_{name}_mosaic.tif'
        arcpy.management.MosaicToNewRaster(files_list, output_folder, output_mosaic, pixel_type="32_BIT_FLOAT", number_of_bands="1", mosaic_method="MEAN")
        print("{} created".format(output_mosaic))
        
