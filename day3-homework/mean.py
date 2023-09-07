#!/usr/bin/env python

import sys
#name = sys.argv[1] # annovations.csv

#f = open( "data.txt" )
#data = f.readlines()
# # data contains a list of strings, one per line

numbers = [1,4,6,3,67,8,4]
moreNumbers = [4,5,6,3]

def average(data):
	addition = sum(data)
	length = len(data)
	return addition/length


print(average(numbers))
print(average(moreNumbers))
