#This code will make a list of rasters in the corresponding ECOSTRESS year folder with the prefix ALEXI_ETdaily
#Then is will iterate thru all the raster files and extract the date and time
#Then it will write a text file with the date and time
import arcpy
import os
from os import listdir, path, mkdir
from datetime import datetime, timedelta
import pytz

ws = "E:/ECOSTRESS/AZ_HUC8/2022/MatchingDates2"
fileout = "E:/ECOSTRESS/AZ_HUC8/ECO22dateandtime_MST_112324.txt"

arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True

#create empty list to store raster file names
rasters = []

#iteratre through files in folder and add to empty list if TIFF format and starts with ALEXI_ETdaily
for file in listdir(ws):
    if file.endswith(".tif") and file.startswith("ALEXI_ETdaily"):
        rasters.append(file)

# Define the time zones
utc = pytz.utc
mst = pytz.timezone("MST")

with open(fileout, "w") as fout:
    fout.write("Date: \n")

    # Iterate through the list and extract dates from the file name, write them into a text document
    for raster in rasters:
        year = int(raster[17:21])
        doy = int(raster[21:24])
        hour = int(raster[24:26])
        date_obj = datetime(year, 1, 1) + timedelta(days=doy - 1, hours=hour)
        
        # Localize the date object to UTC and then convert to MST
        date_obj_utc = utc.localize(date_obj)
        date_obj_mst = date_obj_utc.astimezone(mst)
        
        formatted_date = date_obj_mst.strftime("%Y-%m-%d %H:00")
        fout.write("{0}\n".format(formatted_date))

fout.close()
