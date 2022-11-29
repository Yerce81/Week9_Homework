# Setting workspace environment

arcpy.env.workspace = r'C:\Users\jg198\Desktop\GIS6345_70530\Week9\ArcGIS_Python\LC09_L1TP_040036_20220827_20220827_02_T1'

# Checking to see if workspace is corret

arcpy.ListRasters()

# Print a list of only TIF images
landsatBandList = arcpy.ListRasters("*", "TIF")
for raster in landsatBandList:
    print(raster)

# Finding index number of Band 5
print(landsatBandList.index('LC09_L1TP_040036_20220827_20220827_02_T1_B5.TIF'))
print(landsatBandList.index('LC09_L1TP_040036_20220827_20220827_02_T1_B7.TIF'))

# Creating variable for Band 5 and Band 7

nir_band = landsatBandList[6]
swir_band = landsatBandList[8]

#Checking to see if correct band is output
print(nir_band)

# Creating Raster objects for the NIR and SWIR bands
nir = arcpy.Raster(nir_band)
swir= arcpy.Raster(swir_band)

# creating values for NBR fraction, top and bottom, which will use map algebra to obtain NBR results

topNum = arcpy.sa.Float(nir -swir)
bottomNum = arcpy.sa.Float(nir + swir)

# Divide topnum by bottomNum to get NBR
NBR = topNum / bottomNum


# Saving NBR
NBR.save('NBR_LC09_L1TP_040036_20220827_20220827.TIF')

arcpy.ia.Render(NBR, colormap = 'NDVI')


