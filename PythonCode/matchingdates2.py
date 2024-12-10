import arcpy
import os
from os import listdir, path, mkdir
import shutil

#set workspace and output folder for merged raster files
ws = "E:/ECOSTRESS/AZ_HUC8/2022"
et_ws = "E:/ECOSTRESS/AZ_HUC8/2022/ETALEXI/Combined"
qf_ws = "E:/ECOSTRESS/AZ_HUC8/2021/QualityFlag/Combined"
vz_ws = "E:/ECOSTRESS/AZ_HUC8/2022/ViewZenith/Combined"
output_folder = "E:/ECOSTRESS/AZ_HUC8/2022/MatchingDates2"

arcpy.env.workspace = ws
arcpy.env.overwriteOutput = True

#create empty lists
dailyet = []
etdates = []
qf = []
qf_filtered = []
vz = []
vz_filtered = []

#make a list of all combined ET rasters
for file in listdir(et_ws):
    if file.endswith(".tif"):
        dailyet.append(file)
#copy etdaily tif files to output folder
for et_file in dailyet:
    shutil.copy(path.join(et_ws, et_file), output_folder)
print("Files copied to output folder:", len(listdir(output_folder)))

#make a list of all combined quality flag rasters
for file in listdir(qf_ws):
    if file.endswith(".tif"):
        qf.append(file)

#make a list of all combined view zenith rasters
for file in listdir(vz_ws):
    if file.endswith(".tif"):
        vz.append(file)
    
#extract dates from dailyet and add file names to text file
fileout1 = "E:/ECOSTRESS/AZ_HUC8/2019/etdailynames.txt"
fout1 = open(fileout1, "w")
for dailyet in dailyet:
    etdate = dailyet[17:26]
    etname = dailyet[0:26]
    etdates.append(etdate)
    fout1.write("{0}\n".format(etname))
fout1.close()
print("Text file with etdaily names created.")
et_len = str(len(etdates))
print("Number of files in etdates: " + et_len)
    
#check if date in qf exists in etdates and add to new list, then add file names to text file
fileout2 = "E:/ECOSTRESS/AZ_HUC8/2019/qfnames.txt"
fout2 = open(fileout2, "w")
for qf in qf:
    qfdate = qf[3:12]
    qfname = qf[0:12]
    if qfdate in etdates:
        qf_filtered.append(qf)
        fout2.write("{0}\n".format(qfname))
fout2.close()
print("Text file with quality flag names created.")
qf_len = str(len(qf_filtered))
print("Number of files in qf_filtered: " + qf_len)

#check if date in vz exists in etdates and add to new list, then add file names to text file
fileout3 = "E:/ECOSTRESS/AZ_HUC8/2019/vznames.txt"
fout3 = open(fileout3, "w")
for vz in vz:
    vzdate = vz[3:12]
    vzname = vz[0:12]
    if vzdate in etdates:
        vz_filtered.append(vz)
        fout3.write("{0}\n".format(vzname))
fout3.close()
print("Text file with view zenith names created.")
vz_len = str(len(vz_filtered))
print("Number of files in vz_filtered: " + vz_len)

#copy files from qf_filtered and vz_filtered and uc_filtered to output folder
for file in qf_filtered:
    shutil.copy(path.join(qf_ws, file), output_folder)
print("Files copied to output folder:", len(listdir(output_folder)))

for file in vz_filtered:
    shutil.copy(path.join(vz_ws, file), output_folder)
print("Files copied to output folder:", len(listdir(output_folder)))
