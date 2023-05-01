# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:49:40 2023

@author: gab_a
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trim = pd.read_csv('trim.csv')

plt.rcParams['figure.dpi'] = 300

#%% Restaurants by cuisine

by_cuisine = trim['cuisine'].value_counts()
by_cuisine_most = by_cuisine[ by_cuisine >= 100 ]
print(by_cuisine_most.sort_values(ascending=False))

trim_cuisine = trim[ trim['cuisine'].isin(by_cuisine_most.index) ]

fig,ax = plt.subplots(figsize=(6,10))
sns.set_theme(style="darkgrid")
sns.countplot(data=trim_cuisine,y='cuisine', ax=ax)
ax.set_title('Restaurant Count by Food Type', fontweight = 'bold',  size = 14)
ax.set_xlabel('Count', fontstyle = 'italic', size = 12 )
ax.set_ylabel('Food Type', fontstyle = 'italic', size = 12)
fig.savefig('count_cuisine.png')

#%% Restaurants by borough

by_boro = trim['county'].value_counts()
print(by_boro)

fig,ax = plt.subplots()
sns.set_theme(style="darkgrid")
sns.countplot(data=trim,y='boro',ax=ax, palette = 'magma')
ax.set_title('Restaurant Count by County', fontweight = 'bold', size = 14)
ax.set_xlabel('Count', fontstyle = 'italic', size = 12 )
ax.set_ylabel('County', fontstyle = 'italic', size = 12)
fig.savefig('count_boro.png')

#%% Restaurants by borough and grade

by_boro_grade = trim[['boro','grade']].value_counts().unstack()
by_boro_grade_tot = by_boro_grade.sum(axis='columns')
by_boro_grade_pct = 100*by_boro_grade.div(by_boro_grade_tot,axis='index')

print(by_boro_grade_pct)

fig,ax = plt.subplots()
sns.set_theme(style="darkgrid")
pal = ['green', 'yellow', 'red']
by_boro_grade_pct = by_boro_grade_pct.sort_values('A',ascending=False)
by_boro_grade_pct.plot.barh(ax=ax,stacked=True, color = pal)
ax.set_title('Percent in Each Grade by County', fontweight = 'bold', size = 14)
ax.set_xlabel('Percent', fontstyle = 'italic', size = 12 )
ax.set_ylabel('County', fontstyle = 'italic', size = 12)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
fig.savefig('pct_boro.png')

#%% Restaurants by cuisine and grade

by_cuisine_grade = trim_cuisine[['cuisine','grade']].value_counts().unstack()
by_cuisine_grade_tot = by_cuisine_grade.sum(axis='columns')
by_cuisine_grade_pct = 100*by_cuisine_grade.div(by_cuisine_grade_tot,axis='index')

print(by_cuisine_grade_pct)

fig,ax = plt.subplots(figsize=(6,10))
sns.set_theme(style="darkgrid")
pal = ['green', 'yellow', 'red']
by_cuisine_grade_pct = by_cuisine_grade_pct.sort_values('A',ascending=False)
by_cuisine_grade_pct.plot.barh(ax=ax,stacked=True, color = pal)
ax.set_title('Percent in Each Grade by Food Type', fontweight = 'bold', size = 14)
ax.set_xlabel('Percent', fontstyle = 'italic', size = 12 )
ax.set_ylabel('Food Type', fontstyle = 'italic', size = 12)
sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
fig.savefig('pct_cuisine.png')

#%%

trim['ts'] = pd.to_datetime(trim['ts'])
trim['Year'] = trim['ts'].dt.year
trim['Year'] = trim['Year'].astype(int) # Change the datatype of the year column of trim to an integer.

