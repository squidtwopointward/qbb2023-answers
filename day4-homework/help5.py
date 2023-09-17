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
for i in range(20):
	frequncy2 = fisher(.7,100)
	ax.plot(frequncy2)
plt.show()

histograms = []
for i in range(2000):
	frequency3 = fisher(0.2)
	numberoffrequency = len(frequency3)
	histograms.append(numberoffrequency)
plt.hist(histograms)

plt.show()



#Exercise 3
fig, ax = plt.subplots()


popof50 = []
for i in range(50):
	iterations = fisher(0.3)
	averageof50 = len(iterations)
	popof50.append(averageof50)
	fifty = np.mean(popof50)
fifty_pop.append(fifty)
population = fifty_pop.append(fifty)
print(population)

popof100 = []
for i in range(100):
	iterations1 = fisher(0.3)
	averageof100 = len(iterations1)
	popof100.append(averageof100)
	hundred = np.mean(popof100)
hundred_pop.append(hundred)
population1 = hundred_pop.append(hundred)
print(population1)

popof150 = []
for i in range(150):
	iterations2 = fisher(0.3)
	averageof150 = len(iterations2)
	popof150.append(averageof150)
	onefify = np.mean(popof150)
onefify_pop.append(onefify)
population2 = onefify_pop.append(onefify)
print(population2)

popof200 = []
for i in range(200):
	iterations3 = fisher(0.3)
	averageof200 = len(iterations3)
	popof200.append(averageof200)
	twohundred = np.mean(popof200)
twohundred_pop.append(twohundred)
population3 = twohundred_pop.append(twohundred)
print(population3)

popof250 = []
for i in range(250):
	iterations4 = fisher(0.3)
	averageof250 = len(iterations4)
	popof250.append(averageof250)
	twofifty = np.mean(popof250)
twofifty_pop.append(twofifty)
population4 = twofifty_pop.append(twofifty)
print(population4)


plt.scatter(population, averageof50)
plt.scatter(population1, averageof100)
plt.scatter(population2, averageof150)
plt.scatter(population3, averageof200)
plt.scatter(population4, averageof250)
plt.xlabel("Average Fixation Time")
plt.ylabel("Size of the Population")

plt.show()


avgof50 = []
for i in range(300):
	iterations11 = fisher(0.3)
	averageof501 = len(iterations11)
	avgof50.append(averageof501)
	threehundred = np.mean(avgof50)
threehundred_pop.append(threehundred)
population_threehundred = threehundred_pop.append(threehundred_pop)


avgof100 = []
for i in range(300):
	iterations21 = fisher(0.5)
	averageof1001 = len(iterations21)
	avgof100.append(averageof1001)
	threehundred1 = np.mean(avgof100)
threehundred1_pop.append(threehundred1)
population_threehundred1 = threehundred_pop.append(threehundred1)

avgof150 = []
for i in range(300):
	iterations31 = fisher(0.6)
	averageof1501 = len(iterations31)
	avgof150.append(averageof1501)
	threehundred2 = np.mean(avgof150)
threehundred2.append(threehundred2)
population_threehundred2 = threehundred2.append(threehundred2)

avgof200 = []
for i in range(300):
	iterations41 = fisher(0.1)
	averageof2001 = len(iterations41)
	avgof200.append(averageof2001)
	threehundred3 = np.mean(avgof200)
twohundred3_pop.append(threehundred3)
population_threehundred3 = threehundred3_pop.append(threehundred3)

avgof250 = []
for i in range(300):
	iterations51 = fisher(0.8)
	averageof2501 = len(iterations51)
	avgof250.append(avgof250)
	threehundred4 = np.mean(avgof2501)
threehundred4_pop.append(threehundred4)
population_threehundred4 = threehundred4_pop.append(threehundred4)



plt.scatter(population_threehundred, averageof501)
plt.scatter(population_threehundred1, averageof1001)
plt.scatter(population_threehundred2, averageof1501)
plt.scatter(population_threehundred3, averageof2001)
plt.scatter(population_threehundred4, averageof2501)
plt.xlabel("Average Fixation Time")
plt.ylabel("Allele Frequency")


plt.show()






