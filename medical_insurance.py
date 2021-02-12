# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:29:39 2021

@author: erict
"""

####### Notes #########
#Project guided by Code Academy
#Analyze medical insurance data
#Going to go out of the scope of the project and play around with pandas, since 
#I already have some exposure to that
#Scope to look at:
    #What region has the highest cost
    #What region has the most smokers
    #What region has the highest BMI
####### Notes #########

#import the data
import csv
import pandas as pd
df = pd.read_csv('insurance.csv')
from matplotlib import pyplot as plt
#check data to ensure it loaded properly
#print(df)

#What region has the highest average cost?
#first find the unique regions that the database contains
unique_regions = df['region'].unique()
#print(unique_regions)

#alright now we know that we have southwest, southeast, northwest, and northeast
#let's create our hold variables for each
southwest = 0
southeast = 0
northwest = 0
northeast = 0

#create a zip of the columns we want
test_data = zip(df['region'], df['charges'])

#loop through the data and add to our totals
for item in test_data:
    if item[0] == 'southwest':
        southwest += item[1]
    elif item[0] == 'southeast':
        southeast += item[1]
    elif item[0] == 'northwest':
        northwest += item[1]
    else:
        northeast += item[1]

#convert our unique regions and our values into a dictionary
charges_by_region = {unique_regions[0]: southwest, unique_regions[1]: southeast,
                     unique_regions[2]: northwest, unique_regions[3]: northeast}

#view the data
print(charges_by_region)

#and I just learned that you can plot by dictionary. It obviously needs some
#cleaning; but the Southeast has the highest cost
plt.bar(charges_by_region.keys(), charges_by_region.values())
