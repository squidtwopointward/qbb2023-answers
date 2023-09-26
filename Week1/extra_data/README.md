The `penguins.csv` file contains a simplified version of the Palmer Penguins dataset (https://github.com/allisonhorst/palmerpenguins/) where rows containing missing data have been removed.

The `aau1043_parental_age.csv` file is from the paper (https://www.science.org/doi/10.1126/science.aau1043) and contains ages of the parents of each proband.

The `aau1043_dnm.csv` file is from the same paper as above and contains information about the number and parental origin of each de novo mutation detected in each proband.


Answer to 2.3
#What is the “size” of this relationship? In your own words, what does this mean? Does this match what you observed in your plots in step 6?
# Yes, the size matches the plots. There wasn't much a correlation seen with the naked eye so I didn't expect for the R squared to be high. 

 Is this relationship significant? How do you know?
# Yes the data is significant because the P on absolute T is less than 0.5.


# Answer to 2.4 
# You do a plug and chug for y = B0 + B1x where the Y would be the mutation and the x is age of the parent while the B0 is the intercept. B1 is the slope.
From that you should be able to get your number of paternal DNMs


#Answer to 2.5
#x axis will be distribution of of maternal per proband 


#Answer to 2.6

Ttest_DMNs = sps.ttest_ind(paternal_dmns, maternal_dmns)
print(Ttest_DMNs)

#Step 2.6

What statistical test did you choose? Why?
      I chose the independent sample t test because we are comparing two different things 
      (maternal and paternal) within the same distrubtion (proband_id), so it seemed like the most 
      approicate test.



Was your test result statistically significant? Interpret your result as it relates to the number of paternally
 and maternally inherited DNMs.
	No the results were not significant with a p value of 2.19 with a df of 790.0. That means paternal 
	and maternal dmns are not closely related as we thought. 

