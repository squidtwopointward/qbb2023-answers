#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



origins = pd.read_csv('aau1043_dnm.csv')
# print(origins)

# print(len(origins) # To determine # of rows and columns 
# print(origins.columns) #To determine the names of all the columns 

# origins.info() #More details on the data

# print(type(origins)) #Confirm that data is in dataframe


deNovoCount = {}
for i in range(len(origins)): 
	proband_id = origins.loc[i,'Proband_id']
	parent = origins.loc[i,'Phase_combined']
	if proband_id not in deNovoCount:
		deNovoCount[proband_id] = [0,0]
	if parent == 'mother':
		deNovoCount[proband_id][0]+= 1
	elif parent == 'father':
		deNovoCount[proband_id][1]+= 1


deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])


parental_age = pd.read_csv('aau1043_parental_age.csv',  index_col = 'Proband_id')
#identify what i want from mergeddata
#mergeData[153567]
# print(parental_age)


# print(parental_age)


mergedData = pd.concat([parental_age,deNovoCountDF], axis = 1, join = 'inner')
# print(mergedData)


#identify what i want from mergeddata


print(mergedData.loc[153567, : ])


