#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import sys

# Exercise 1

allele = []
#Made a function of how to randomly get the frequency with the Wright-Fisher 
def fisher(freq, pop = 100):
	##We want to prevent the passing of 1 and 0
	##Record the starting figure
	allele = [freq]


	while freq > 0 and freq < 1:
		freq = np.random.binomial(2*pop, freq)/ (2*pop)
		allele.append(freq)
	return(allele)




allelefrequency = fisher(0.3)
#This should be my x axis also number of generations which is 58.
allelegenerations = len(allelefrequency)
print(allelegenerations)
# y axis would be the frequency of the allele
fig, ax = plt.subplots()
for i in range(1):
	frequency1 = allelefrequency
	ax.plot(frequency1)
plt.show()

np.random.seed(24)

def BoyinMotions(numberofsteps):
	x = 0
	y = 0 

	xlist = [x]
	ylist = [y]

	for time in range(numberofsteps):
		xdisplacement = np.random.uniform(-1,1)
		ydisplacement = np.random.uniform(-1,1)

		x = x + xdisplacement
		y = y + ydisplacement

		xlist.append(x)
		ylist.append(y)
	return(xlist,ylist)

fig, ax = plt.subplots()
for i in range(30):
	alleletrajectory = BoyinMotions(400)
	xposition = alleletrajectory[0]
	yposition = alleletrajectory[1]
	ax.plot(xposition,yposition)
plt.show()


#Exercise 2
fig, ax = plt.subplots()
for i in range(50):
	iterations = fisher(0.3)
# ax.plot(iterations)

fig, ax = plt.subplots()
for i in range(100):
	iterations1 = fisher(0.3)
# ax.plot(iterations1)

fig, ax = plt.subplots()
for i in range(150):
	iterations2 = fisher(0.3)
# ax.plot(iterations2)

fig, ax = plt.subplots()
for i in range(200):
	iterations3 = fisher(0.3)
# ax.plot(iterations3)

fig, ax = plt.subplots()
for i in range(250):
	iterations4 = fisher(0.3)
# ax.plot(iterations4)


ty = len(iterations)
ty1 = len(iterations1)
ty2 = len(iterations2)
ty3 =len(iterations3)
ty4 = len(iterations4)

generations = (ty, ty1, ty2, ty3, ty4)
frequencies = (iterations, iterations1, iterations2, iterations3, iterations4)


fig, ax = plt.subplots()
# ax.plot(allelefrequency)

plt.show()






