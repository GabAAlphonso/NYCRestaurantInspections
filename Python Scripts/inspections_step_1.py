# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:53 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 1

# This is the first of a series of scripts which will look at NYC restaurant inspection results
# with particular focus on the assigned grades (based on food violations scores) and food type/cuisine
# across the five boroughs.

# This script focuses on the following:
#   a. Removing unwanted columns
#   b. Renaming column names
#   c. Dropping records  of establishments with no violations, and 
#   d. Determining the number of violations (critical and non-critical) by 
#      inspection date, establishment and borough. 

# Note: the following words are used interchangeably throughout the scripts: restaurant,
# establishment and facility.  

# Import Pandas to begin
import pandas as pd

#%% Read Raw Data and Standardize Column Names

# Create a list of variables which must be read as strings
str_list = ['CAMIS', 'ZIPCODE','Cenus Tract']

# Build a dictionary with the elements of str_list as keys and str as each entry's value.
str_cols = {s: str for s in str_list}

# Read the csv file "NYC_Restaurant_Inspection_Results.csv" downloaded on March 8, 2023 into a dataframe
# called raw.
raw = pd.read_csv('NYC_Restaurant_Inspection_Results.csv', dtype = str_cols)

# There are some empty columns as well as data we don't need.
# Drop these from the dataframe
usable = raw.drop(columns = ['PHONE', 'Community Board','Council District',
                       'BIN', 'BBL', 'NTA', 'Location Point'])

# Create a dictionary of new column names. By standardizing the column names we are removing spaces in 
# coloumn names, keeping text lowercase and making it easier to use in subsequent code. 
new_cols = {'INSPECTION DATE': 'insp_date', 'INSPECTION TYPE': 'insp_type', 
            'CRITICAL FLAG': 'critical_flag',
            'CUISINE DESCRIPTION': 'cuisine', 'VIOLATION CODE': 'vio_code',
            'VIOLATION DESCRIPTION': 'vio_des', 'Census Tract': 'census_track', 
            'Longitude': 'long', 'Latitude': 'lat', 'GRADE DATE': 'grade_date', 
            'GRADE': 'grade', 'BORO': 'boro', 'SCORE': 'score', 'CAMIS': 'camis',
            'STREET':'street', 'ACTION': 'action', 'DBA':'dba', 'BUILDING': 'building'}

# Rename the column in usable dataframe
usable = usable.rename(columns = new_cols)

#%% Begin Data Cleaning

# Drop records with '1/1/1900' inspection date. Why?
# These are new establishments that have not yet received an inspection, and therefore
# have no violations (scores and assigned grades).
usable = usable[usable['insp_date'] !='01/01/1900']

# Drop records with 'N' grades. These are restaurants that have not had a 
# graded inspection. Until a restaurant has a graded inspection, it is
# listed as 'Not Yet Graded' on the Health Department website.
usable = usable[usable['grade'] !='N']

# What's the number of dropped records?
print('Initial No. of Dropped Records:', len(raw) - len(usable))
# This number is expected to increase as the data cleaning process continues...

#%% Initial Analysis

# Group by facility and inspection date
grouped_facil_inspec = usable.groupby(['dba', 'insp_date'])

# What's the number of violations (critical and non-critical) per inspection date?
cv_by_date = grouped_facil_inspec.size()

# What's the total number of violations (critical and non-critical) for each restaurant?
cv_by_facil = usable.groupby('camis').size()

# Drop records with '0' in the borough column.
# Why? For the most part, these are data entry errors.
usable = usable[usable['boro'] != '0']

# What's the total number of violations (critical and non-critical) across each of the boroughs?
cv_by_boro = usable.groupby('boro').size()

# Write usable to pickle file
usable.to_pickle('usable.pkl')