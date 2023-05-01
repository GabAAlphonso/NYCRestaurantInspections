# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:52:09 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 6

# Here we use GeoPandas to help us handle the geospatial data and begin the data visualization
# process.
# As the aim is to show the geospatial distribution of the facilities by grade, we will need
# to select NYC counties from US shapefile.

# Import the geopandas module to begin.
import geopandas as gpd

#  EPSG number for UTM 18N

utm18n = 26918

#  GEOIDs for NYC counties

nyc_geoids = [
    "36005", # Bronx
    "36047", # Kings
    "36061", # New York
    "36081", # Queens
    "36085", # Richmond
    ]

#  Read the county file

all_co = gpd.read_file("cb_2021_us_county_500k.zip")

#  Select NYC and project to UTM 18N for convenience later

nyc_co = all_co[ all_co['GEOID'].isin(nyc_geoids) ]
nyc_co = nyc_co.to_crs(utm18n)

#  Save the result

nyc_co.to_file('nyc_counties.gpkg',layer='counties')