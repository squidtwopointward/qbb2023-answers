#!/usr/bin/env python
import sys
import numpy as np
fellow = "/Users/cmdb/Desktop/swc-python/data/inflammation-01.csv"


# def haterows(fname, index):
# 	f = open(fname, "r")
# 	fname = f.readlines()
# 	patient = fname[index]
# 	patient = patient.rstrip('\n')
# 	patient = patient.split(',')
# 	patient_int = []
# 	for item in patient:
# 		patient_int.append(int(item))
# 	#print(patient_int)
# 	avg = sum(patient_int)/len(patient_int)
# 	return avg

# print(haterows(fellow, 4))

def haterows(fname, index, index2):
	f = open(fname, "r")
	fname = f.readlines()
	patient = fname[index]
	patient2 = fname[index2]
	patient = patient.rstrip('\n')
	patient2 = patient2.rstrip('\n')
	patient = patient.split(',')
	patient2 = patient2.split(',')
	patient_int = []
	for item in patient:
		patient_int.append(int(item))
	patient_int2 = []
	for item in patient2:
		patient_int2.append(int(item))
	#print(patient_int)
	return(np.array(patient_int2)-(np.array(patient_int)))
		
print(haterows(fellow, 6, 4))