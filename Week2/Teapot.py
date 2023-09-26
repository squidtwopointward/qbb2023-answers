#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.formula.api as smf
import statsmodels.api as sm



##Execise 1
#_ in number will be ignored.


def simulation(coverage, lengthofgenome, readlength, figname):
	coveragearray = np.zeros(lengthofgenome)
	
	low = 0
	high = lengthofgenome - readlength

	reads = int(coverage * lengthofgenome /readlength) #This gives use a integer 
	start_position = np.random.randint(low=low , high= high +1 , size = reads)
	# print(startposition)


	for start in start_position:
		coveragearray[start: start + readlength] += 1

	x = np.arange(0, max(coveragearray)+ 1)

	sim_0cov = lengthofgenome - np.count_nonzero(coveragearray)
	sim_0cov_pct = 100 * sim_0cov / lengthofgenome

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
	print(f'This is {sim_0cov_pct}% of the genome')


	#Get the poisson distribution Mean coverage would be coverage
	# Just to see the arrray 
	# y_poisson = print(stats.poisson.pmf(x, mu= coverage))

	#This should put it on the same histogram scale. This is Poisson distribution 
	y_poisson = (stats.poisson.pmf(x, mu= coverage) * lengthofgenome)

	#This is for the normal distrubution 
	y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage) * lengthofgenome)
	print(y_normal)


	fig, ax = plt.subplots()
	ax.hist(coveragearray, bins = x, align = 'left', label = 'Simulation')
	ax.plot(x, y_poisson, label = 'Poisson')
	ax.plot(x, y_normal, label = 'Normal')
	ax.set_xlabel('Number of Reads')
	ax.set_ylabel('Frequency of BasePairs')
	ax.legend()
	fig.tight_layout()
	fig.savefig('ex1_10x_cov1.png')
	plt.show()


simulation(10, 1_000_000, 100, 'ex1_10x_cov.png')
print(simulation)