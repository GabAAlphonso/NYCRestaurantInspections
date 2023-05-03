# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:49:40 2023

@author: gab_a
"""
# NYC Restaurant Inspection Results - STEP 6

# This is the final script for this project. 

# Let's generate two summary figures: one that gives the number of restaurants by 
# food type/cuisine and  another that gives the count of resturants by borough.

# For the sake of clarity, do note that 'cuisine' from now onward is referred to as 'food type/cuisine'.
# The dataset references food in terms of 'cuisine' which we know refers to a cooking style or method
# that is distinctive of a country or region. However, donuts, sandwiches, juice, smoothies, etc. are not
# really cuisine but rather types of food. Hence the distinction moving forward.

# Import Pandas, Matplotlib and Seaborn to begin.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trim = pd.read_csv('trim.csv')

plt.rcParams['figure.dpi'] = 300

#%% Restaurants by Food type/Cuisine

by_cuisine = trim['cuisine'].value_counts()
by_cuisine_most = by_cuisine[ by_cuisine >= 100 ]
print(by_cuisine_most.sort_values(ascending=False))

trim_cuisine = trim[ trim['cuisine'].isin(by_cuisine_most.index) ]

fig,ax = plt.subplots(figsize=(6,10))
sns.set_theme(style="darkgrid")
sns.countplot(data=trim_cuisine, y='cuisine', ax=ax, ec = 'black')
ax.set_title('Restaurant Count by Food Type/Cuisine', fontweight = 'bold',  size = 14)
ax.set_xlabel('Count', fontweight = 'bold', size = 12 )
ax.set_ylabel('Food Type/Cuisine', fontweight = 'bold', size = 12)

fig.savefig('count_cuisine_foodtype.png')

#%% Restaurants by Borough

by_boro = trim['boro'].value_counts()
print(by_boro)

fig,ax = plt.subplots()
sns.set_theme(style="darkgrid")
sns.countplot(data=trim,y='boro',ax=ax, palette = 'magma', ec = 'black')
ax.set_title('Restaurant Count by Borough', fontweight = 'bold', size = 14)
ax.set_xlabel('Count', fontweight = 'bold', size = 12 )
ax.set_ylabel('Borough', fontweight = 'bold', size = 12)
fig.savefig('count_boro.png')



