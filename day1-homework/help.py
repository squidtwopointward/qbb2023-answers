#!/usr/bin/env python
import numpy 


#Exercise #1
#Label the dataset

f = open("/Users/cmdb/Desktop/swc-python/data/inflammation-01.csv", "r")

lines = f.readlines()

patients = []
#index = 0 
for line in lines:	
	line = line.rstrip()
	line_list = line.split(",")
	#print(line_list)
	patients.append(line_list)

#Print patient 5 data by itself
#print(patients[4])

# Print the 1st, 5th, and last
print(patients[4][0])
print(patients[4][9])
print(patients[4][39])


#Exercise 2

avg = []
for ind_patients in patients:
	all = 0 
	for day in ind_patients:
	 day_int =int(day)
	all += day_int
ind_avg = all/len(ind_patients)
avg.append(ind_avg)

print(avg[0:9])
	
#Exercise 3


print(numpy.max(avg))
print(numpy.min(avg))


#Exercise 4

patients = []
#index = 0 
for line in lines:	
	line = line.rstrip()
	line_list = line.split(",")
	#print(line_list)
	patients.append(line_list)
	patients_int = int(patients)
difference = (sum(patients_int[5])) - (sum(patients_int[1]))
print(difference)
