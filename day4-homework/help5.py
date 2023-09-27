#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import statsmodels.api as sm

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
print(f'This is the {allelegenerations} of generations')
# y axis would be the frequency of the allele
fig, ax = plt.subplots()
for i in range(1):
	frequency1 = allelefrequency
	ax.plot(frequency1)
	ax.set_xlabel('Number of Generations')
	ax.set_ylabel('Frequency')
	fig.savefig('Plot')

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

ax.set_xlabel('Number of Steps')
ax.set_ylabel('Allele Trajectory')

plt.savefig('Plot3.png')

plt.show()



#Exercise 2

fig, ax = plt.subplots()
for i in range(20):
	frequncy2 = fisher(.7,100)
	ax.plot(frequncy2)
	ax.set_xlabel('Frequency of Alleles')
	ax.set_ylabel('Movement of Trajectory')
	fig.savefig('Multiple Trajectory')

plt.show()

histograms = []
for i in range(2000):
	frequency3 = fisher(0.2)
	numberoffrequency = len(frequency3)
	histograms.append(numberoffrequency)
plt.hist(histograms)
ax.set_xlabel('Number of Frequency')
ax.set_ylabel('Allele Frequency')


plt.savefig('Plot4.png')

plt.show()



#Exercise 3
fig, ax = plt.subplots()


popof50 = []
for i in range(50):
	iterations = fisher(0.3)
	averageof50 = len(iterations)
	popof50.append(averageof50)
	fifty = np.mean(popof50)
popof50.append(fifty)
population = popof50.append(fifty)
print(population)

popof100 = []
for i in range(100):
	iterations1 = fisher(0.3)
	averageof100 = len(iterations1)
	popof100.append(averageof100)
	hundred = np.mean(popof100)
popof100.append(hundred)
population1 = popof100.append(hundred)
print(population1)

popof150 = []
for i in range(150):
	iterations2 = fisher(0.3)
	averageof150 = len(iterations2)
	popof150.append(averageof150)
	onefify = np.mean(popof150)
popof150.append(onefify)
population2 = popof150.append(onefify)
print(population2)

popof200 = []
for i in range(200):
	iterations3 = fisher(0.3)
	averageof200 = len(iterations3)
	popof200.append(averageof200)
	twohundred = np.mean(popof200)
popof200.append(twohundred)
population3 = popof200.append(twohundred)
print(population3)

popof250 = []
for i in range(250):
	iterations4 = fisher(0.3)
	averageof250 = len(iterations4)
	popof250.append(averageof250)
	twofifty = np.mean(popof250)
popof250.append(twofifty)
population4 = popof250.append(twofifty)
print(population4)


plt.scatter(population, averageof50)
plt.scatter(population1, averageof100)
plt.scatter(population2, averageof150)
plt.scatter(population3, averageof200)
plt.scatter(population4, averageof250)
plt.xlabel("Average Fixation Time")
plt.ylabel("Size of the Population")
plt.savefig('Plot5.png')

plt.show()


avgof501 = []
threehundred = []
for i in range(300):
	iterations11 = fisher(0.3)
	averageof501 = len(iterations11)
	avgof501.append(averageof501)
	threehundred = np.mean(avgof501)
avgof501.append(threehundred)
threehundred.append(threehundred)


avgof1001 = []
threehundred1 = []
for i in range(300):
	iterations21 = fisher(0.5)
	averageof1001 = len(iterations21)
	avgof1001.append(averageof1001)
	threehundred1 = np.mean(avgof1001)
avgof1001.append(threehundred1)
threehundred1.append(threehundred1)

avgof1501 = []
threehundred2 = []
for i in range(300):
	iterations31 = fisher(0.6)
	averageof1501 = len(iterations31)
	avgof1501.append(averageof1501)
	threehundred2 = np.mean(avgof1501)
avgof1501.append(threehundred2)
threehundred2.append(threehundred2)

avgof2001 = []
threehundred3 = []
for i in range(300):
	iterations41 = fisher(0.1)
	averageof2001 = len(iterations41)
	avgof2001.append(averageof2001)
	threehundred3 = np.mean(avgof2001)
avgof2001.append(threehundred3)
threehundred3.append(threehundred3)

avgof2501 = []
threehundred4 = []
for i in range(300):
	iterations51 = fisher(0.8)
	averageof2501 = len(iterations51)
	avgof2501.append(averageof2501)
	threehundred4 = np.mean(avgof2501)
avgof2501.append(threehundred4)
threehundred4.append(threehundred4)

fig, ax = plt.subplots()
plt.plot(threehundred, avgof501)
plt.plot(threehundred1, avgof1001)
plt.plot(threehundred2, avgof1501)
plt.plot(threehundred3, avgof2001)
plt.plot(threehundred4, avgof2501)
plt.xlabel("Average Fixation Time")
plt.ylabel("Allele Frequency")
plt.savefig('Plot of allele frequency vs. time to fixation.png')

plt.show()






