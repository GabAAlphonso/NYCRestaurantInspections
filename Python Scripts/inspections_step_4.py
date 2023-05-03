# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:55 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 4

# This script focuses on the following:
#   a. Assigns grades A, B or C based on the DoH scores

# Note: the four types of gradable inspections are divided into pairs.
# Why? In cases where the initial inspection is 14 points and over, a re-inspection of
# the facility is required. This re-inspection grade is what is posted at the entrance of 
# the facility, for the public. 
# Looking at the data in pairs is an attempt to assign grades based on the most recent records,
# keeping in mind that the recent grades of some facilities may be based on re-inspection. 


# Import Pandas to begin.
import pandas as pd

usable = pd.read_pickle('usable.pkl')

#%% Pre-permit Inspections

# Figure out the scores and grades for pre-permit (operational)
check_pre_permit1 = usable.query("insp_type =='Pre-permit (Operational) / Initial Inspection'")
check_pre_permit2 = usable.query("insp_type =='Pre-permit (Operational) / Re-inspection'")
all_pre  = pd.concat([check_pre_permit1, check_pre_permit2])

all_pre['ts'] = pd.to_datetime(all_pre['insp_date']) # The insp_date is currently 
# sorted as string. To sort correctly, convert them into datetime value

all_pre = all_pre.set_index('ts', append = True).sort_index()
by_pre_permit = all_pre.groupby(['camis', 'score','insp_type', 'grade']).sum() 
# What's the purpose
# of this???

preperm_analysis = all_pre.reset_index(drop=False)[['camis', 'std_dba','building', 'street','boro','cuisine','insp_type', 'ts', 'grade', 'score', 'lat', 'long']].drop_duplicates().copy()
preperm_analysis = preperm_analysis.sort_values(['camis', 'ts'])
preperm_analysis = preperm_analysis.drop_duplicates(subset = 'camis', keep='last')

# Grades and scores fields may be inconsistent with each other because of limitations or errors in the 
# data systems. Scores of 0 - 13 are given a grade 'A', 14 -47 are given a grade 'B' and 28+, grade C.
# Note: on re-inspection, a score of 14 to 27 points means that a restaurant receives both a 'B' grade
# and a 'Grade Pending' card (Grade pending is denoted by 'Z'). It's also the same when a restaurant
# receives both a 'C' grade and 'Grade Pending' card.
# Try to assign grades to match given scores.
preperm_analysis.loc[preperm_analysis['score']<=13, 'grade'] = 'A' 
preperm_analysis.loc[(preperm_analysis['score']>13) & (preperm_analysis['score']<28) , 'grade'] = 'B' 
preperm_analysis.loc[preperm_analysis['score']>=28, 'grade'] = 'C'

#%% Cycle Inspections

# Figure out the scores and grades for cycle inspections (initial and reinspection)
check_cycle_insp1 = usable.query("insp_type =='Cycle Inspection / Initial Inspection'")
check_cycle_insp2 = usable.query("insp_type =='Cycle Inspection / Re-inspection'")
all_cycle  = pd.concat([check_cycle_insp1, check_cycle_insp2])

all_cycle['ts'] = pd.to_datetime(all_cycle['insp_date'])# The insp_date is currently 
# sorted as string. To sort correctly, convert them into datetime value

all_cycle = all_cycle.set_index('ts', append = True).sort_index()
by_all_cycle = all_cycle.groupby(['camis', 'score','insp_type', 'grade']).sum()

cycle_analysis = all_cycle.reset_index(drop=False)[['camis', 'std_dba','building', 'street','boro','cuisine','insp_type', 'ts', 'grade', 'score', 'lat', 'long']].drop_duplicates().copy()
cycle_analysis = cycle_analysis.sort_values(['camis', 'ts'])
cycle_analysis = cycle_analysis.drop_duplicates(subset = 'camis', keep='last')

# Grades and scores fields may be inconsistent with each other because of limitations or errors in the 
# data systems. Scores of 0 - 13 are given a grade 'A', 14 -47 are given a grade 'B' and 28+, grade C.
# Note: on re-inspection, a score of 14 to 27 points means that a restaurant receives both a 'B' grade
# and a 'Grade Pending' card (Grade pending is denoted by 'Z'). It's also the same when a restaurant
# receives both a 'C' grade and 'Grade Pending' card.
# Try to assign grades to match given scores.
cycle_analysis.loc[cycle_analysis['score']<=13, 'grade'] = 'A' 
cycle_analysis.loc[(cycle_analysis['score']>13) & (cycle_analysis['score']<28) , 'grade'] = 'B' 
cycle_analysis.loc[cycle_analysis['score']>=28, 'grade'] = 'C'

#%% Joining both dataframes
trim  = pd.concat([preperm_analysis, cycle_analysis])

#%% Create a column in trim called 'County'
# The boroughs of Queens and the Bronx are also Queens County and Bronx County. 
# The other three counties are named differently from their boroughs: Manhattan is in New York 
# County, Brooklyn is in Kings County, and Staten Island is in Richmond County.

# For now, let's make this distinction. The data can now be filtered by either county or
# borough in Tableau or any other visualization tool.
trim.loc[trim['boro']=='Bronx', 'county'] = 'Bronx'
trim.loc[trim['boro']=='Brooklyn', 'county'] = 'Kings'
trim.loc[trim['boro']=='Manhattan', 'county'] = 'New York'
trim.loc[trim['boro']=='Queens', 'county'] = 'Queens'
trim.loc[trim['boro']=='Staten Island', 'county'] = 'Richmond'

#%% New Column to 'trim'

# Add a new column called 'year' to trim that will extract year from the timestamp column
trim['year'] = trim['ts'].dt.year
trim['year'] = trim['year'].astype(int) # Change the datatype of the year column of trim to an integer.

#%% Write trim to csv file for later use in the visualization tool
trim.to_csv('trim.csv')

usable.to_pickle('usable.pkl')