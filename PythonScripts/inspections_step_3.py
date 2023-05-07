# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:33:54 2023

@author: gab_a
"""

# NYC Restaurant Inspection Results - STEP 3

# This script focuses on the following:
#   a. Removing non-gradable inspection types, special program and administrative
#      violations that do not contribute towards overall score and grade

# The dataframe is narrowed down to the four gradable inspections only.

# Import Pandas to begin
import pandas as pd

usable = pd.read_pickle('usable.pkl')

#%% Removal of non-gradable inspections and pending grades

# Now, organize the scores and grades for the facilities based on inspection type.

# There are many things we have to do here!
# Take a deep breath and begin...

# Special Program and Administrative violations (violation codes 15-22) do NOT
# contribute towards SCORE and GRADE.
# Filter these records from the dataframe.
usable = usable[usable['vio_code'] !='18-01']

# Take a look at the inspection types for facilities with Grades P and Z.
check_P = usable.query("grade =='P'")
check_Z = usable.query("grade =='Z'")

# Drop records with 'P' Grades.
# Why? These are facilities closed on initial inspection, and will get a reopening inspection
# before operations can be resumes.
# Reopening inspections are not gradable and scores do no determine inspection cycle grade.
# P = Grade pending issued on re-opening following an initial inspection that resulted in a closure.
usable = usable.query("grade != 'P'")

# Compliance inspections are scored but do not determine grade.
# For now, filter records with the words 'Compliance' in the 
# inspection type. Examples include: Second Compliance or Compliance Inspection, etc.
usable = usable[usable['insp_type'].str.contains("Compliance")==False]

# The inspection type "Pre-permit (Operational) / Reopening Inspection" that is assigned a score and 
# grade 'Z'should be removed.
# Why? For this inspection type, the score and grade do not contribute to the regular cycle inspection.
# Note this applies primarily to new facilities that failed to comply with Health Codes prior to permit approval and 
# were closed by DOH. Before the establishment can be re-opened it must undego a reopening inspection.
is_reopening_z = (usable['insp_type'] == "Pre-permit (Operational) / Reopening Inspection") & (usable['grade'] == 'Z')
usable = usable[~is_reopening_z]

# As per the information file, there are four gradable inspections: 'cycle inspection/initial inspection',
# 'cycle inspection/re-inspection', 'pre-permit (operational)/initial inspection' and  'pre-permit (operational)/re-inspection'.
# For the purpose of determining the grades based on the conditons outlined in EXAMPLE 1 on Page 4, we will also keep inspection
# type, 'cycle inspection/reopening inspection'.
# Let's keep records with these inspection types only (for now).
keepers = [
   'Cycle Inspection / Re-inspection',  
   'Cycle Inspection / Initial Inspection'
   'Pre-permit (Operational) / Initial Inspection', 
   'Pre-permit (Operational) / Re-inspection',   
   ]
keep_it = usable['insp_type'].isin(keepers)
usable = usable[ keep_it ]

#%%
usable.to_pickle('usable.pkl')