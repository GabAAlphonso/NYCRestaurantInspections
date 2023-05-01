# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:36:20 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 7

# As the aim is to show the geospatial distribution of the facilities by grade, we will need
# to select NYC census tract from US shapefile.

# Import the geopandas and pandas modules to begin.
import geopandas as gpd
import pandas as pd

#  EPSG number for UTM 18N

utm18n = 26918

#  Read the census tract file

all_co = gpd.read_file("cb_2021_36_tract_500k.zip")

#  GEOIDs for NYC census tracts
bronx = all_co[all_co['GEOID'].str.contains("36005")==True]
kings = all_co[all_co['GEOID'].str.contains("36047")==True]
ny = all_co[all_co['GEOID'].str.contains("36061")==True]
queens = all_co[all_co['GEOID'].str.contains("36081")==True]
richmond = all_co[all_co['GEOID'].str.contains("36085")==True]

# Merge the county data
nyc_geoids = pd.concat([bronx, kings, ny, queens, richmond])

#  Select NYC and project to UTM 18N for convenience later?????

nyc_geoids = nyc_geoids.to_crs(utm18n)

#  Save the result

nyc_geoids.to_file('nyc_counties.gpkg',layer='tracts')