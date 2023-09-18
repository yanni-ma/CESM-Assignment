# load in all of the libraries you need
# if you don't have these you will need to install them:
#   pip install matplotlib
#   pip install numpy
#   pip install pyproj
#   pip install pyshp
#   pip install basemap
import matplotlib.pyplot as plt
import numpy as np
import netCDF4
from netCDF4 import Dataset as NetCDFFile
from mpl_toolkits.basemap import Basemap

# load in the netcdf file
nc = NetCDFFile('tas_Amon_CESM-CAM5.1-FV_piControl_r1i1p1_000101-005012.nc')
lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time = nc.variables['time'][:]
tas = nc.variables['tas'][:] # 2 meter temperature (you should change this depending on the file you want to load)

# World map in the Robinson projection
m = Basemap(projection='robin',lon_0=0,resolution='i') # resolutions: c - crude, l - low, i - intermediate, h - high, f - full
lons,lats= np.meshgrid(lon-180,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = m(lons,lats)
tasmean=np.average(tas,axis=0,weights=None) # creating a time average so that we can show it on a map

# the file I tested this with was plotted on lons 0:360 but the map projection wants lons -180:180 so we have to swap them around
I=np.shape(tasmean)
tasmean2=np.zeros(I)
tasmean2[:,int(I[1]/2):]=tasmean[:,0:int(I[1]/2)]
tasmean2[:,0:int(I[1]/2)]=tasmean[:,int(I[1]/2):]

temp = m.contourf(x,y,tasmean2) # filled contour plot
temp2 = m.contour(x,y,tasmean2) # line contour plot
m.drawcoastlines(linewidth=0.25) # adds coastlines
m.drawparallels(np.arange(-90.,120.,30.)) # adds some latitude lines
m.drawmeridians(np.arange(0.,360.,60.)) # adds some longitude lines
cb = m.colorbar(temp,"bottom", size="5%", pad="2%") # adds a colorbar
plt.show() # shows the plot
plt.savefig('mapplot.png') # saves the plot
