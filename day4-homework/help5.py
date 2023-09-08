#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

import sys


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

#allelefrequency = fisher(0.3)



fig, ax = plt.subplots()
for i in range(50):
	iterations = fisher(0.3)
ax.plot(iterations)

fig, ax = plt.subplots()
for i in range(100):
	iterations1 = fisher(0.3)
ax.plot(iterations1)

fig, ax = plt.subplots()
for i in range(150):
	iterations2 = fisher(0.3)
ax.plot(iterations2)

fig, ax = plt.subplots()
for i in range(200):
	iterations3 = fisher(0.3)
ax.plot(iterations3)

fig, ax = plt.subplots()
for i in range(250):
	iterations4 = fisher(0.3)
ax.plot(iterations4)


plt.show()


ty = len(iterations)
ty1 = len(iterations1)
ty2 = len(iterations2)
ty3 =len(iterations3)
ty4 = len(iterations4)

print(ty, ty1, ty2, ty3, ty4)








