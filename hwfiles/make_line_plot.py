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

# The latitudes we have are at the centers but to compute grid box areas we need edges
latedges=np.ma.array(-90)
latedges2=np.ma.append(latedges,(lat[:-1]+(lat[3]-lat[2])/2)[:])
latedges3=np.ma.append(latedges2,np.ma.array(90))

r=6371000
colats=(np.pi)/2-latedges3*(np.pi)/180
dphi=(lon[3]-lon[2])*(np.pi)/180
area=np.abs(np.diff(np.cos(colats)))*dphi*(r**2)
w=np.transpose(np.tile(area,(I[1],1))) # area of each lon/lat grid box

tastimeseries=np.average(np.average(tas,axis=1,weights=area),axis=1,weights=None) # weighted average over latitudes, regular average over longitudes
J=np.size(tastimeseries)

fig_line=plt.figure()
plt.plot(range(0,J),tastimeseries,color='black') # makes a line plot with the number of times on the x-axis
plt.xlabel('Month')
plt.ylabel('Temperature (K)')
plt.show() # shows the plot
plot.savefig('lineplot.png') # saves the plot

