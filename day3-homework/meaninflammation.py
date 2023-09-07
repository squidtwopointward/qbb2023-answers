#!/usr/bin/env python
import sys
import numpy as np
fellow = "/Users/cmdb/Desktop/swc-python/data/inflammation-01.csv"

#fname = sys.argv[1]

# patient = []
# for i in f:
# 	i_stripped = i.rstrip("\n")
# 	i_int = int(i_stripped)
# 	hello.append(i_int)
# print(patient)



# patients = []
# #index = 0 
# for i in f:	
# 	line = line.rstrip()
# 	line_list = line.split(",")
# 	#print(line_list)
# 	patients.append(line_list)
# 	print(patients)


# avg = []
# for ind_patients in patients:
# 	total = 0
# 	days = int(patients)
# 	sum += int(ind_patients)
# 	avg = sum/length(ind_patients)[0:9]
# 	print(avg)

#fname = fellow.readlines()

# patients = []
# for i in fname:	
# 	f_strip = i.rstrip()
# 	f_split = f_strip.split(",")
# 	patients.append(f_split)
# print(patients)
	
# patient = []
# for i in patients:
# 	patients_val = int(patients)
# 	patient.append(patients_val)

# print(patient)

def haterows(fname, index):
	f = open(fname, "r")
	fname = f.readlines()
	patient = fname[index]
	patient = patient.rstrip('\n')
	patient = patient.split(',')
	patient_int = []
	for item in patient:
		patient_int.append(int(item))
	#print(patient_int)
	avg = sum(patient_int)/len(patient_int)
	return avg

print(haterows(fellow, 4))



	# f_int = int(f_split)
# 	# patients.append(f_int)
# print(patients)

#Print patient 5 data by itself
#print(patients[4])

# # Print the 1st, 5th, and last
# print(patients[4][0])
# print(patients[4][9])
# print(patients[4][39])
