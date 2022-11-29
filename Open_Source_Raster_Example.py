#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import rioxarray as rxr
import earthpy as et


# In[4]:


# Prettier plotting with seaborn
sns.set(font_scale=1.5, style='whitegrid')


# In[6]:


# Get data and set working directory
et.data.get_data("colorado-flood")
os.chdir(os.path.join(et.io.HOME,'Desktop'))


# In[7]:


#Define relative path to file
lidar_dem_path = os.path.join("colorado-flood", "spatial", "boulder-leehill-rd", "pre-flood", "lidar", "pre_DTM.tif")

# Open lidar dem
lidar_dem_xr = rxr.open_rasterio(lidar_dem_path, masked=True).squeeze()
lidar_dem_xr


# In[9]:


# define relative path to file
lidar_dsm_path = os.path.join("colorado-flood", "spatial", "boulder-leehill-rd", "pre-flood", "lidar", "pre_DSM.tif")

# Open lidar dem
lidar_dsm_xr = rxr.open_rasterio(lidar_dsm_path, masked=True).squeeze()
lidar_dsm_xr                      


# In[11]:


# Are the bpunds the same?
print("Is the spatial extend the same?", lidar_dem_xr.rio.bounds() == lidar_dsm_xr.rio.bounds())

# Is the resolution the same?
print("Is the resolution the same?", lidar_dem_xr.rio.resolution() == lidar_dsm_xr.rio.resolution())


# In[12]:


# Calculate canopy height model
lidar_chm_xr = lidar_dsm_xr - lidar_dem_xr

# Plot the data
f, ax = plt.subplots(figsize=(10, 5))
lidar_chm_xr.plot(cmap="Greens")
ax.set(title="Canopy Height Model for Lee Hill Road Pre-Flood")
ax.set_axis_off()
plt.show()


# In[13]:


# Plot histogram of range values
lidar_chm_xr.plot.hist()
plt.show()


# In[16]:


print('CHM min value: ', np.nanmin(lidar_chm_xr))
print('CHM max value: ', np.nanmax(lidar_chm_xr))


# In[18]:


data_path = os.path.join("colorado-flood", "spatial", "outputs")

if os.path.exists(data_path):
    print("the directory", data_path, "exists!")
else:
    os.makedirs(data_path)


# In[20]:


# Make sure output data has a crs & no data valued defined
print("The crs is", lidar_chm_xr.rio.crs)
print("The no data value is", lidar_chm_xr.rio.nodata)


# In[21]:


pre_chm_data_path = os.path.join(data_path, "pre-flood-chm.tif")
pre_chm_data_path


# In[22]:


# Export data to geotiff
lidar_chm_xr.rio.to_raster(pre_chm_data_path)


# In[23]:


# Re-open the data
lidar_chm_data = rxr.open_rasterio(pre_chm_data_path, masked=True).squeeze()
lidar_chm_data


# In[ ]:




