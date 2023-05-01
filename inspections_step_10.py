# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 03:24:41 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 10

# Now consider if there were trends in the inspection year and the grades issued.
# If the output does not make sense - delete this script.

# The first part of this process invloves extracting the year bit of the timestamp (ts).

# Import modules to begin
import pandas as pd
import seaborn as sns

#%%

# Read the data from the files we've been working on
usable = pd.read_pickle('usable.pkl')

trim = pd.read_csv('trim.csv')

#%%

# Add a new column called year to trim that will extract year from the timestamp column

trim['ts'] = pd.to_datetime(trim['ts'])
trim['Year'] = trim['ts'].dt.year

#%%

# Plot a line chart

sns.lineplot(data = trim, x='Year', y="score")

trim.plot.line(x="Year", y="grade")
