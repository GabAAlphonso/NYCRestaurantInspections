# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:55 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 5

# We have a new dataframe 'trim' which is more or less the data we will visualize
# using Tableau.

# Let's do some additional cleaning of trim and add a few columns for better visualization:
    # Filter out duplicate and missing records for latitude and longitude coordinates 
    # Spell out abbreviations in street addresses, where possible
    # Standardize and clean-up the street addresses, where possible
    # Create three new variables to color code inspection grades in Tableau
    # Count the number of resturants with unsatisfactory grades ('B' and 'C')

# Import the pandas module to begin.
import pandas as pd

usable = pd.read_pickle('usable.pkl')

#%% Drop duplicate records in trim

trim = pd.read_csv('trim.csv', index_col=[0]) # the second argument removes the Unamed:0 column

trim = trim.sort_values('camis')
trim = trim.drop_duplicates(subset = 'camis', keep='last') # Most recent record will be kept

#%% Spell out abbreviations and fix spacing in street addresses
fix_list = {
    'Ave':'Avenue',
    'Rd': 'Road',
    'St': 'Street',
    'Plz': 'Plaza',
    'Prkway': 'Parkway',
    'Pl': 'Place',
    'Blvd': 'Boulevard',
    'Ct':'Center',}

def fix(old):
    words = old.split()
    new = []
    for word in words:
        if word in fix_list:
            new.append(fix_list[word])
        else:
            new.append(word)
    return ' '.join(new)
fixed = trim['street'].apply(fix)     

trim['street'] = fixed   

#%% Drop records with latitude and longitude values of '0' and 'nan'(missing)

trim = trim.dropna(subset = ['lat', 'long']) # drops records where latitude and longitude points are missing
trim = trim.loc[~((trim['lat'] == 0) & (trim['long'] == 0))] # drops records where latitude and longitude
# equal to 0

#%% New variables for color selection into Tableau Tool Tips

grade = trim['grade']
trim['tt_a'] = grade.where(grade == 'A', "")
trim['tt_b'] = grade.where(grade == 'B', "")
trim['tt_c'] = grade.where(grade == 'C', "")


#%% Write file to csv
trim.to_csv('trim.csv')

usable.to_pickle('usable.pkl')