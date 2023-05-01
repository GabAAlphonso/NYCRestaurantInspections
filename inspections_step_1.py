# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:53 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 1

# This is the first of a series of scripts which simply look at NYC restaurant inspection results
# with particular focus on the assigned grades (based on food violations scores) and restuarant type
# (based on cuisine ) across the five boroughs.

# This script focuses on removing unwanted columns, renaming column names, dropping records 
# of establishments with no violations, and determining the number of violations
# (critical and non-critical) by inspection date, facility and borough. 

# Import the pandas and matplotlib modules to begin.
import pandas as pd
import matplotlib.pyplot as plt

# Create a list of variables which must be read as strings
str_list = ['CAMIS', 'ZIPCODE','Cenus Tract']

# Build a dictionary with the elements of str_list as keys and str as each entry's value.
str_cols = {s: str for s in str_list}

# Set-up the Pandas DataFrame by reading the NYC_Restaurant_Inspection_Results.csv into a
# a new variable called inspections.
raw = pd.read_csv('NYC_Restaurant_Inspection_Results.csv', dtype = str_cols)

# There are some empty columns as well as data we don't need.
# Drop these from the dataframe
usable = raw.drop(columns = ['PHONE', 'Community Board','Council District',
                       'BIN', 'BBL', 'NTA', 'Location Point'])

# Create a dictionary of new column names
new_cols = {'INSPECTION DATE': 'insp_date', 'INSPECTION TYPE': 'insp_type', 
            'CRITICAL FLAG': 'critical_flag',
            'CUISINE DESCRIPTION': 'cuisine', 'VIOLATION CODE': 'vio_code',
            'VIOLATION DESCRIPTION': 'vio_des', 'Census Tract': 'census_track', 
            'Longitude': 'long', 'Latitude': 'lat', 'GRADE DATE': 'grade_date', 
            'GRADE': 'grade', 'BORO': 'boro', 'SCORE': 'score', 'CAMIS': 'camis',
            'STREET':'street', 'ACTION': 'action', 'DBA':'dba', 'BUILDING': 'building'}

# Rename the column in usable dataframe
usable = usable.rename(columns = new_cols)

# Drop records with '1/1/1900' inspection date. Why?
# These are new establishments that have not yet received an inspection, and therefore
# have no violations (scores and assigned grades).
usable = usable[usable['insp_date'] !='01/01/1900']

# Drop records with 'N' grades. These are facilites that have not had a 
# graded inspection. Until a restaurant has a graded inspection, it is
# listed as 'Not Yet Graded' on the Health Department website.
usable = usable[usable['grade'] !='N']

# What's the number of dropped records?
print('Initial No. of Dropped Records:', len(raw) - len(usable))
# This number is expected to increase as the data cleaning process continues

#%%
# Group by facility and inspection date
grouped_facil_inspec = usable.groupby(['dba', 'insp_date'])

# What's the number of violations (critical and non-critical) per inspection date?
cv_by_date = grouped_facil_inspec.size()

# What's the total number of violations (critical and non-critical) for each facility?
cv_by_facil = usable.groupby('camis').size()

# Drop records with '0' in the borough column.
# Why? For the most part, these are data entry errors.
usable = usable[usable['boro'] != '0']

# What's the total number of violations (critical and non-critical) across each of the boroughs
cv_by_boro = usable.groupby('boro').size()

# Write usable to pickle file
usable.to_pickle('usable.pkl')