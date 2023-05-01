# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 20:37:43 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 8

# 

# Import the geopandas module to begin.
import geopandas as gpd

#  EPSG number for UTM 18N

utm18n = 26918

#  Read the census tract file

all_co = gpd.read_file("cb_2021_36_tract_500k.zip")

#  GEOIDs for NYC census tracts
bronx = all_co[all_co['GEOID'].str.contains("36005")==True]

#  Select NYC and project to UTM 18N for convenience later?????

bronx = bronx.to_crs(utm18n)

#  Save the result
bronx.to_file('nyc_counties.gpkg',layer='bronx')
#%%
#  GEOIDs for NYC census tracts
kings = all_co[all_co['GEOID'].str.contains("36047")==True]

#  Select NYC and project to UTM 18N for convenience later?????

kings = kings.to_crs(utm18n)

#  Save the result
kings.to_file('nyc_counties.gpkg',layer='kings')
#%%
#  GEOIDs for NYC census tracts
ny = all_co[all_co['GEOID'].str.contains("36061")==True]

#  Select NYC and project to UTM 18N for convenience later?????

ny = ny.to_crs(utm18n)

#  Save the result
ny.to_file('nyc_counties.gpkg',layer='ny')
#%%
#  GEOIDs for NYC census tracts
queens = all_co[all_co['GEOID'].str.contains("36081")==True]

#  Select NYC and project to UTM 18N for convenience later?????

queens = queens.to_crs(utm18n)

#  Save the result
queens.to_file('nyc_counties.gpkg',layer='queens')
#%%
#  GEOIDs for NYC census tracts
richmond = all_co[all_co['GEOID'].str.contains("36085")==True]

#  Select NYC and project to UTM 18N for convenience later?????


richmond = richmond.to_crs(utm18n)

#  Save the result
richmond.to_file('nyc_counties.gpkg',layer='richmond')