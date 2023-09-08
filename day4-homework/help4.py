#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import sys

# #We wanted to go through the list 3 times and print (1,2,3,4) 3 times 
# # newlist = []

# list1 = [1, 2, 3, 4]


# # for i in range(len(list)*3):
# # 	newlist.append(i)
# # print(newlist)

# tracklist = []


# while len(tracklist)<12:
# 	for j in list1:
# 		print(j)
# 		tracklist.append(j)
# print(tracklist)

# ^^^^^^^^^^^^ Morning Exercise


##Some numnber of steps 
#each time, step amoeba moves between 1 cm L or R
#Each time, step amoeba moves between 1 cm U or D

#Define the start position of my amoeba

#For each time step:
# move up or down 
# move left or right 
# Store a list in the empty list

##Return to the user:
##The position of my amoeba over time

#numpy has a random funciton (np.random.uniform(-1,1))


def slowmotion(numberofsteps):
	x = 0
	y = 0

	xlist = [x]
	ylist =[y]

	for timepoint in range(numberofsteps):
		#How far do we move 
		ydisplacement = np.random.uniform(-1,1)
		xdisplacement = np.random.uniform(-1,1)

		x = x + xdisplacement
		y = y + ydisplacement

		xlist.append(x)
		ylist.append(y)
	return[xlist, ylist]


#trajectory = (slowmotion(200))

#print(trajectory)

# xposition = trajectory[0]
# yposition = trajectory[1]


# fig, ax = plt.subplots()
# for i in range(20):
# 	trajectory = slowmotion(200)

# 	xposition = trajectory[0]
# 	yposition = trajectory[1]
# 	ax.plot(xposition,yposition)
# #ax.scattor(xposition,yposition)

# plt.show()
#^^^^^^^^ Example did with Andrew

# Wright Fisher Assumption
# contanct population 
# random mating 
# no selection 
# no mutation 
# everyone reproduces in each generation

# Wright Fisher: The Bionomial
# n = the number of chromosomes
# p = the frequency of the allele
# #numpy.random.bionomial(n,p)


# Get starting frequency and a population size ( n= start, p = start )
# #Get a random allele frequency by using the bionomial distrub
# Convert number of success to a frequency
# Store allele frequency  in all previous generation 


# Use while statement n has to either == 1or 0 therefore the code has to stop and give me the list of everything
#return a list allele frequency at the each point
# Number of generation to fixation is the length of the list 


allele = []

def fisher(freq, pop = 100):
	##We want to prevent the passing of 1 and 0
	##Record the starting figure
	allele = [freq]


	while freq > 0 and freq < 1:
		freq = np.random.binomial(2*pop, freq)/ (2*pop)
		allele.append(freq)
	return(allele)



allelefrequency = fisher(0.3)

print(allelefrequency)

#How to get the number of generations
print(len(allelefrequency))

# fig, ax = plt.subplots()

# ax.plot(allelefrequency)

# plt.show()

#print(fisher(0.2))

# fig. ax = plt.subplots()

# ax.plot = (fisher)

# plt.show()








# 		x = x + xchange
# 		y = y + ychange





