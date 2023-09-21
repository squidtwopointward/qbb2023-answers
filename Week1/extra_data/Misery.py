#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm




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


#Scatter Plot for Maternal and Paternal 

fig, ax = plt.subplots()
fig, ax.scatter(mergedData.loc[:,'Mother_age'], mergedData.loc[:,'maternal_dnm'])
ax.set_xlabel('Age of Mother')
ax.set_ylabel('Maternal DNM')

maternal_dmns = mergedData["maternal_dnm"]
# print(maternal_dmns)

paternal_dmns = mergedData["paternal_dnm"]
# print(paternal_dmns)
# fig.savefig('ex2_a.png')


fig, ax = plt.subplots()
fig, ax.scatter(mergedData.loc[:,'Father_age'], mergedData.loc[:,'paternal_dnm'])
ax.set_xlabel('Age of Father')
ax.set_ylabel('Paternal DNM')

# fig.savefig('ex2_b.png')

# plt.show()

#Linear Regression for maternal 

mother_model = smf.ols(formula = 'maternal_dnm ~ 1 + Mother_age', data = mergedData)
results = mother_model.fit()

# print(results.summary())


#Answer to 2.3
# What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 6?
# Yes, the size matches the plots. There wasn't much a correlation seen with the naked eye so I didn't expect for the R squared to be high. 

# Is this relationship significant? How do you know?
# Yes the data is significant because the P on absolute T is less than 0.5.


# Answer to 2.4 
# I believe it'll be like 78% since the R squared for materal data is about 22%



#x axis will be distribution of of materal per proband 

fig, ax = plt.subplots()


ax.hist(paternal_dmns, label = "Paternal DNMs", bins = 30, alpha = 0.5)
ax.hist(maternal_dmns, label = "Maternal DNMs", bins = 30, alpha = 0.5)
ax.set_xlabel('Distribution of Proband')
ax.set_ylabel('Frequency of Probands')
ax.set_title('Number of Probands De Novo Mutations')
ax.legend()


plt.show()



 








