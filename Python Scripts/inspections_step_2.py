# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:54 2023

@author: gab_a
"""
# NYC Restaurant Inspection Results - STEP 2

# This script focuses on the following:
#   a. Data cleaning
#   b. Standardizing restaurant names
#   c. Do initial analyses on the number of violations in facilities with multiple 
#      locatios across the five boroughs

# Import Pandas to begin.
import pandas as pd

#%% Standardize Names

usable = pd.read_pickle('usable.pkl')

# Create a new dataframe with only CAMIS, facility name and borough
# Be sure to remove duplicates and make a copy of this dataframe.
locations = usable[['camis','dba','boro']].drop_duplicates().copy()

# Build a simplified version of the DBA names such that punctuations are removed.
# This will help to standardize names of facilities.
# For example, right now Dunkin Donuts has multiple name variations like
# Dunkin/DUNKIN'.
std_dba = usable['dba'].str.replace(r"'[Ss]", 's', regex = True)
std_dba = std_dba.str.replace(r'\W', ' ', regex = True)
std_dba = std_dba.apply(lambda x: ' '.join(x.upper().split()))

# Add std_dba as a column to locations dataframe.
locations['std_dba'] = std_dba

#%% Standardize Facility Street Information

# Take a look at the data in this column. Street information is all in capital letters
# This will not make for good visualization on Tableau.
# Capitalize each word in the 'street' column
usable['street'] =  usable['street'].str.title()

#%% Some Analysis

# Possibly, there are facilities with multiple locations across NYC.
# Compare the number of violations of these facilties.
# Do they differ?
camis_by_dba = locations.groupby(['std_dba','boro']).size()
camis_by_dba.name = 'locations'
camis_by_dba = camis_by_dba.unstack('boro')

# Determine the number of missing records in camis_by_dba and then drop from dataframe.
camis_by_dba = camis_by_dba.query("std_dba != '' ")
# There was only one record

num_boro = camis_by_dba.notna().sum(axis='columns') 
# counts the number violations for each facility

# Add the std_dba to the trimmed dataframe and drop the DBA column in this same DF.
usable= usable.copy()
usable['std_dba'] = std_dba
usable2 = usable.drop(columns = 'dba')

# Index this Dataframe by CAMIS and std_dba
usable = usable2.set_index(['camis', 'std_dba'])

# Write usable to pickle file
usable.to_pickle('usable.pkl')